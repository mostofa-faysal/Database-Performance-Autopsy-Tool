"""
Canonical execution plan node representation.

This module defines the normalized internal structure used across
all analysis layers. It is intentionally engine-agnostic and immutable.

Design choice:
- We include an `extra` field to carry engine-specific or less common
  attributes without constantly evolving the core schema.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass(frozen=True)
class PlanNode:
    """
    Normalized representation of a single execution plan node.

    This structure captures both planner estimates and actual execution
    metrics when available (EXPLAIN ANALYZE).

    All reasoning and diagnostics operate exclusively on this model.
    """

    # Core node identity
    node_type: str

    # Planner estimates
    startup_cost: float
    total_cost: float
    plan_rows: int
    plan_width: int

    # Runtime metrics (None if not ANALYZE)
    actual_startup_time: Optional[float]
    actual_total_time: Optional[float]
    actual_rows: Optional[int]
    loops: Optional[int]

    # Relation / index metadata
    relation_name: Optional[str]
    index_name: Optional[str]

    # Logical predicates
    filter_condition: Optional[str]
    join_condition: Optional[str]

    # Child nodes in execution order
    children: List["PlanNode"]

    # Engine-specific or non-core attributes
    extra: Dict[str, Any]
