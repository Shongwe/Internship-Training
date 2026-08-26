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

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError("Task file contains invalid JSON.") from error

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

    def delete(self, task_id: int) -> bool:
        """Delete a task by its ID and save the changes."""
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(index)
                self.save()
                return True

        return False

    def get_all(self) -> list[Task]:
        """Return all stored tasks."""
        return self.tasks

    def get_by_id(self, task_id: int) -> Task | None:
        """Return a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def _get_next_id(self) -> int:
        """Return the next available task ID."""
        if not self.tasks:
            return 1

        return max(task.id for task in self.tasks) + 1
