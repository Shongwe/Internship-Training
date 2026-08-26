import pytest
from cli_task_manager_sln.task import Task


def test_task_initialization():
    task = Task(id=1, description="Write internship report", completed=False)
    assert task.id == 1
    assert task.description == "Write internship report"
    assert task.completed is False


def test_task_to_dict():
    task = Task(id=2, description="Prepare slides", completed=True)
    data = task.to_dict()
    assert isinstance(data, dict)
    assert data["id"] == 2
    assert data["description"] == "Prepare slides"
    assert data["completed"] is True


def test_task_from_dict():
    data = {
        "id": 3,
        "description": "Submit assignment",
        "completed": False,
        "priority": "normal",
        "created_at": "2026-08-26T12:00:00"
    }
    task = Task.from_dict(data)
    assert isinstance(task, Task)
    assert task.id == 3
    assert task.description == "Submit assignment"
    assert task.completed is False
    assert task.priority == "normal"


def test_task_mark_completed():
    task = Task(id=4, description="Review code", completed=False)
    task.completed = True
    assert task.completed is True
