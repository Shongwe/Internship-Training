# Week 03 Reflection

## Overview
This week focused on strengthening both **backend API development** and **algorithmic problem solving**. I worked on building a simple data API with FastAPI, added validation using Pydantic v2, and expanded integration tests to cover CRUD operations and edge cases. Alongside that, I solved three classic algorithm exercises: *Container With Most Water*, *Integer to Roman*, and *Valid Sudoku*.

---

## Key Learnings

### FastAPI & Testing
- Learned how to structure a FastAPI project with `app.py`, `routes.py`, `models.py`, and `validators.py`.
- Migrated from deprecated `@validator` to `@field_validator` in Pydantic v2.
- Built **10+ integration tests** using `pytest` to validate endpoints:
  - Create, list, update, delete items
  - Validation errors (blank name, negative price, missing price)
  - Edge cases (ID increments, not found errors)

### Algorithms
- **Container With Most Water**: Practiced two‑pointer optimization, understanding why moving the shorter pointer is greedy but correct.
- **Integer to Roman**: Applied greedy string building with subtractive notation patterns.
- **Valid Sudoku**: Used sets to track duplicates across rows, columns, and 3×3 boxes. Learned how to calculate box indices with `(i // 3) * 3 + (j // 3)`.

### Debugging & Tooling
- Fixed `datetime.utcnow()` deprecation by switching to `datetime.now(UTC)`.
- Resolved Pylance type warnings by importing `List` and `Set` from `typing`.
- Learned how Python package naming affects imports (`simple-data-api` vs `simple_data_api`).
- Practiced organizing exercises into consistent folder structures with `solution.py` + `test_solution.py`.

---

## Challenges
- Import errors due to folder naming (`-` vs `_`).
- Pylance warnings about unknown types in sets.
- Managing pytest fixtures vs global `client` object.
- Keeping tests isolated while ensuring IDs increment correctly.

---

## Wins
- All API tests now pass with no functional errors.
- Each algorithm exercise has clean, tested solutions.
- Improved confidence in type annotations and linter‑friendly code.
- Built a repeatable workflow: **solution → test_solution → pytest validation**.

---