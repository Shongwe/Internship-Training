# Week 3 Reflection


Balancing API persistence with file management was the toughest part. Debugging why `data.json` was being created in different folders depending on where Uvicorn was run required careful attention to relative vs. absolute paths. It wasn’t just about writing endpoints — it was about understanding how the environment interacts with the code.


- Make persistence more configurable and robust (e.g., environment variables or config files for storage path).
- Add a `clear_all()` or reset endpoint for testing.
- Separate persistence logic into a dedicated service layer so routes don’t depend directly on file I/O.
- Consider migrating from JSON to SQLite/PostgreSQL for scalability and concurrency safety.

- Authentication (basic token or OAuth) to secure endpoints.
- Pagination metadata (`page`, `limit`, `total_pages`) in responses.
- Swagger/OpenAPI documentation with examples for each endpoint.
- Logging and monitoring to track requests and errors.
- Unit + integration tests for edge cases, not just happy paths.

- Difference between safe vs. idempotent methods (GET vs. PUT/PATCH/DELETE).
- Proper use of status codes (201 for creation, 404 for not found, 422 for validation errors).
- Stateless communication in REST APIs.
- JSON serialization/deserialization as the core of client‑server exchanges.
- Importance of consistent error responses in API design.

- Concurrency and race conditions in file‑based storage — what happens if multiple requests hit the API at once?
- Advanced error handling patterns (global exception handlers, custom error classes).
- Designing APIs that remain RESTful yet flexible when requirements change (nested resources, partial updates).
- Structuring APIs for scalability when moving from local JSON storage to a real database.