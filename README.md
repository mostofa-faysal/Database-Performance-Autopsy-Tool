# Database Performance Autopsy Tool

A tool that analyzes slow queries, index usage, and schema design, then produces human-readable diagnoses. It explains **why** performance is bad, not just **that** it is.

## Core components

- Query plan parsing
- Index hit/miss analysis
- Schema anti-pattern detection
- Recommendation engine with confidence levels

## Repository structure

```
db-diagnostician/
├─ analysis/
│  ├─ plan/
│  │  ├─ parser.py
│  │  ├─ normalizer.py
│  │  └─ nodes.py
│  ├─ indexes/
│  │  └─ index_analysis.py
│  ├─ schema/
│  │  └─ antipatterns.py
│  ├─ inference/
│  │  ├─ findings.py
│  │  ├─ aggregator.py
│  │  └─ confidence.py
│  └─ explanation/
│     └─ renderer.py
├─ rules/
│  └─ postgres.yaml
├─ fixtures/
│  └─ explain_plans/
├─ tests/
├─ api/
│  └─ main.py
└─ README.md
```

## Signals

- Strong SQL + systems knowledge
- Analytical depth
- Senior-level debugging instincts
