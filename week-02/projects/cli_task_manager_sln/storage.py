import json
from pathlib import Path

from cli_task_manager_sln.task import Task


class TaskStorage:
    """Handle loading and saving tasks to a JSON file."""

    def __init__(self, filename: str = "tasks.json") -> None:
        """Initialize storage and load existing tasks."""
        self.filename = Path(filename)
        self.tasks = self.load()

    def load(self) -> list[Task]:
        """Load tasks from the JSON file."""
        if not self.filename.exists():
            return []

        with self.filename.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return [Task.from_dict(task) for task in data["tasks"]]

    def save(self) -> None:
        """Save the current tasks to the JSON file."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "next_id": self._get_next_id(),
        }

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    def add(self, task: Task) -> None:
        """Add a task and save the updated task list."""
        self.tasks.append(task)
        self.save()

    def delete(self, task_id: int) -> None:
        """Delete a task by its ID and save the changes."""
        self.tasks = [
            task for task in self.tasks if task.id != task_id
        ]
        self.save()

    def get_all(self) -> list[Task]:
        """Return all stored tasks."""
        return self.tasks

    def _get_next_id(self) -> int:
        """Return the next available task ID."""
        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1