# AI-Router Agent Rules

## Mission

Build a production-ready AI Router for code analysis.

Always prefer maintainability over quick fixes.

---

## Coding Style

- Python 3.11+
- Full type hints
- Pydantic v2
- Async first
- Ruff compliant
- pytest required

---

## Project Rules

Never change a public interface unless necessary.

Fix the root cause instead of adding workarounds.

Always update all dependent files when changing an interface.

Never leave duplicated code.

Always use dependency injection.

---

## Testing

Before finishing any task:

1. Run Ruff
2. Run pytest
3. Fix all failing tests

---

## Refactoring Rules

Prefer small focused classes.

Prefer composition over inheritance.

Avoid global state.

Avoid singleton unless necessary.

---

## Project Structure

app/
api/
providers/
router_engine/
scanner/
analyzers/
rag/
services/

tests/

---

## Current Goal

Finish Router Engine.

Then Provider.

Then Scanner.

Then Analyzer.

Then RAG.

Then Multi-Agent.

---

## Response Style

When modifying code:

- Read the whole package first.
- Modify multiple files if necessary.
- Keep project consistent.
- Return production quality code.