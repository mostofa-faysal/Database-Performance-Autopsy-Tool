# Database Performance Autopsy Tool

A diagnostic system that analyzes database query execution plans and schema metadata to explain **why** queries are slow, not just **that** they are slow.

Most database tools surface metrics. This project focuses on **root-cause analysis and human-readable reasoning**, bridging the gap between raw execution plans and senior-level database performance diagnosis.

This is **not** a query optimizer. It is a deterministic, explainable diagnostic and reasoning tool.

---

## Problem Statement

Modern databases expose highly detailed execution plans, but interpreting them requires deep SQL and systems expertise. Developers often know a query is slow but struggle to answer:

* Why did the planner choose this execution path?
* Why was an index ignored?
* Is the issue data distribution, schema design, or query structure?
* What change would *actually* improve performance?

This tool is designed to answer those questions directly.

---

## Project Goals

* Parse and normalize database execution plans
* Detect performance anti-patterns (index misuse, cardinality errors, schema issues)
* Produce human-readable diagnoses backed by concrete evidence
* Separate raw signals from inferred conclusions to preserve explainability
* Remain deterministic, testable, and auditable

---

## Current Scope

### Supported Databases

* PostgreSQL (initial focus)

### Analysis Level

* Single-query analysis
* Execution plan–driven diagnostics
* Rule- and heuristic-based reasoning (no black-box ML)

### Project Status

* Execution plan parsing implemented
* Index usage analysis in progress
* Inference and explanation layers under development

---

## Repository Structure

```
Database-Performance-Autopsy-Tool/
├─ db-diagnostician/        # Project / package root
│  ├─ analysis/             # Parsing and analysis logic
│  ├─ fixtures/             # Real EXPLAIN plan samples
│  ├─ tests/                # Deterministic test suite
│  └─ README.md             # Package-level documentation
└─ README.md                # Project overview (this file)
```

All development and execution occur inside `db-diagnostician/`.

---

## Design Principles

* **Explainability first**
  Every diagnosis must be traceable to concrete evidence in the execution plan or schema metadata.

* **Signals before conclusions**
  Low-level observations are emitted before higher-level reasoning or recommendations.

* **Separation of concerns**
  Parsing, analysis, inference, and explanation are isolated layers.

* **Conservative by default**
  The tool avoids speculative recommendations and explicitly surfaces confidence levels.

---

## Intended Audience

* Backend engineers
* Data engineers
* Senior developers diagnosing production performance issues
* Learners studying database internals and query planners

---

## Roadmap (High Level)

* Index hit/miss analysis
* Cardinality misestimation detection
* Schema anti-pattern detection
* Root-cause inference aggregation
* Natural language explanation rendering
* CLI and API interfaces

---

## Non-Goals

* Automatic query rewriting
* Autonomous schema migration
* Black-box performance scoring
* Database-specific “tuning magic”

---

## License

TBD

---

## Author

Built as a systems-focused, explainability-driven project to demonstrate deep SQL knowledge, database internals, and diagnostic reasoning.

---
