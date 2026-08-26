import pytest
from cli_task_manager_sln.task import Task
from cli_task_manager_sln.storage import TaskStorage


@pytest.fixture
def storage(tmp_path):
    # Use a temporary file so tests don’t touch your real tasks.json
    test_file = tmp_path / "tasks.json"
    return TaskStorage(filename=test_file)


def test_add_and_get_all(storage):
    task = Task(id=1, description="Test task", completed=False)
    storage.add(task)
    tasks = storage.get_all()
    assert len(tasks) == 1
    assert tasks[0].description == "Test task"
    assert tasks[0].completed is False


def test_delete_task(storage):
    task1 = Task(id=1, description="Task A", completed=False)
    task2 = Task(id=2, description="Task B", completed=False)
    storage.add(task1)
    storage.add(task2)

    storage.delete(1)
    tasks = storage.get_all()
    assert len(tasks) == 1
    assert tasks[0].id == 2


def test_save_and_load(storage):
    task = Task(id=1, description="Persisted task", completed=False)
    storage.add(task)

    # Reload from file
    new_storage = TaskStorage(filename=storage.filename)
    tasks = new_storage.get_all()
    assert len(tasks) == 1
    assert tasks[0].description == "Persisted task"


def test_next_id(storage):
    task1 = Task(id=1, description="First", completed=False)
    storage.add(task1)
    task2 = Task(id=storage._get_next_id(), description="Second", completed=False)
    storage.add(task2)

    ids = [t.id for t in storage.get_all()]
    assert ids == [1, 2]
