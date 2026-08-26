from datetime import datetime

VALID_PRIORITIES = {"low", "normal", "high"}


class Task:
    """Represent a task in the task manager."""

    def __init__(
        self,
        id: int,
        description: str,
        completed: bool = False,
        priority: str = "normal",
        created_at: str | None = None,
    ) -> None:
        """Initialize a task."""
        if not description.strip():
            raise ValueError("Task description cannot be empty.")

        if priority not in VALID_PRIORITIES:
            raise ValueError("Priority must be low, normal, or high.")

        self.id = id
        self.description = description
        self.completed = completed
        self.priority = priority
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert the task to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create a Task instance from a dictionary."""
        return cls(
            id=data["id"],
            description=data["description"],
            completed=data["completed"],
            priority=data["priority"],
            created_at=data["created_at"],
        )
