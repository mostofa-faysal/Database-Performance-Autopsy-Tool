"""
PostgreSQL EXPLAIN (FORMAT JSON) plan parser.

This module performs *structural parsing only*.
It does not infer performance problems or optimization advice.

Assumptions:
- Input is generated using EXPLAIN (ANALYZE, FORMAT JSON)
- JSON structure follows PostgreSQL documentation
"""

from typing import Dict, Any, List
from analysis.plan.nodes import PlanNode


def parse_explain_json(explain_json: Dict[str, Any]) -> PlanNode:
    """
    Parses a PostgreSQL EXPLAIN (FORMAT JSON) output into a PlanNode tree.

    This function is intentionally strict:
    - Missing required fields raise KeyError
    - No default guessing or inference is performed

    :param explain_json: Raw JSON output from EXPLAIN (FORMAT JSON)
    :return: Root PlanNode
    """
    try:
        plan = explain_json[0]["Plan"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("Invalid EXPLAIN JSON structure") from exc

    return _parse_plan_node(plan)


def _parse_plan_node(node: Dict[str, Any]) -> PlanNode:
    """
    Recursively parses a single plan node and its children.

    PostgreSQL may nest child plans under different keys
    depending on node type. We normalize this here.
    """

    children = []
    for key in ("Plans", "InitPlan", "Subplans"):
        if key in node:
            # PostgreSQL represents children as a list under these keys
            children.extend(_parse_plan_node(child) for child in node[key])

    return PlanNode(
        node_type=node["Node Type"],
        startup_cost=node["Startup Cost"],
        total_cost=node["Total Cost"],
        plan_rows=node["Plan Rows"],
        plan_width=node["Plan Width"],
        actual_startup_time=node.get("Actual Startup Time"),
        actual_total_time=node.get("Actual Total Time"),
        actual_rows=node.get("Actual Rows"),
        loops=node.get("Actual Loops"),
        relation_name=node.get("Relation Name"),
        index_name=node.get("Index Name"),
        filter_condition=node.get("Filter"),
        join_condition=node.get("Join Filter"),
        children=children,
        # We store remaining attributes for later analysis layers
        extra=_extract_extra_fields(node),
    )


def _extract_extra_fields(node: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts non-core attributes from a plan node.

    This prevents early schema lock-in and allows future analyzers
    to consume engine-specific metadata without parser changes.
    """

    core_keys = {
        "Node Type",
        "Startup Cost",
        "Total Cost",
        "Plan Rows",
        "Plan Width",
        "Actual Startup Time",
        "Actual Total Time",
        "Actual Rows",
        "Actual Loops",
        "Relation Name",
        "Index Name",
        "Filter",
        "Join Filter",
        "Plans",
        "InitPlan",
        "Subplans",
    }

    return {k: v for k, v in node.items() if k not in core_keys}
