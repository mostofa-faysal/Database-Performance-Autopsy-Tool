# Database Performance Autopsy Tool

A diagnostic tool that analyzes database query execution plans and schema metadata to explain **why** queries are slow, not just **that** they are slow.

Most database tools surface metrics. This project focuses on **root-cause analysis** and **human-readable explanations**, bridging the gap between raw query plans and senior-level database reasoning.

---

## Problem Statement

Modern databases provide detailed execution plans, but interpreting them requires deep systems and SQL expertise. Developers often know a query is slow but struggle to answer:

* Why did the planner choose this execution path?
* Why was an index ignored?
* Is the problem data distribution, schema design, or query structure?
* What change would actually improve performance?

This tool aims to answer those questions directly.

---

## Project Goals

* Parse and normalize database execution plans
* Detect performance anti-patterns (index misuse, cardinality errors, schema issues)
* Produce **human-readable diagnoses** with supporting evidence
* Separate *signals* from *conclusions* to maintain explainability
* Remain deterministic, testable, and auditable

This is not a query optimizer. It is a diagnostic and reasoning tool.

---

## Current Scope

**Databases**

* PostgreSQL (initial focus)

**Analysis Level**

* Single-query analysis
* Execution plan–driven diagnostics
* Rule- and heuristic-based reasoning (no black-box ML)

**Status**

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
└─ README.md                # (this file)
```

All development and execution happens inside `db-diagnostician/`.

---

## Design Principles

* **Explainability first**
  Every diagnosis must be traceable to concrete evidence.

* **Signals before conclusions**
  Low-level findings are emitted before higher-level reasoning.

* **Separation of concerns**
  Parsing, analysis, inference, and explanation are isolated layers.

* **Conservative by default**
  The tool avoids speculative recommendations and surfaces confidence explicitly.

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
* Database-specific tuning magic

---

## License

TBD

---

## Author

Built as a systems-focused, explainability-driven project to demonstrate deep SQL, database internals, and diagnostic reasoning.

---
