import json
from analysis.plan.parser import parse_explain_json
from analysis.plan.nodes import PlanNode


def test_simple_seq_scan_parsing():
    """
    Verifies that a basic sequential scan plan is parsed into
    a normalized PlanNode without inference or mutation.
    """
    with open("fixtures/explain_plans/simple_seq_scan.json") as f:
        explain = json.load(f)

    plan = parse_explain_json(explain)

    assert isinstance(plan, PlanNode)
    assert plan.node_type == "Seq Scan"
    assert plan.relation_name == "users"
    assert plan.actual_rows == 9500
    assert plan.children == []
