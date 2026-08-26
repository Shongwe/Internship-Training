import pytest
from click.testing import CliRunner
from cli_task_manager_sln.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def tmp_storage(tmp_path):
    return tmp_path / "tasks.json"


def test_add_task(runner, tmp_storage):
    result = runner.invoke(cli, ["--file", str(tmp_storage), "add", "Test task"])
    assert result.exit_code == 0
    assert "Test task" in result.output


def test_list_tasks(runner, tmp_storage):
    runner.invoke(cli, ["--file", str(tmp_storage), "add", "Task A"])
    runner.invoke(cli, ["--file", str(tmp_storage), "add", "Task B"])
    result = runner.invoke(cli, ["--file", str(tmp_storage), "list"])
    assert result.exit_code == 0
    assert "Task A" in result.output
    assert "Task B" in result.output


def test_done_task(runner, tmp_storage):
    runner.invoke(cli, ["--file", str(tmp_storage), "add", "Finish report"])
    result = runner.invoke(cli, ["--file", str(tmp_storage), "done", "1"])
    assert result.exit_code == 0
    assert "marked as complete" in result.output.lower()


def test_delete_task(runner, tmp_storage):
    runner.invoke(cli, ["--file", str(tmp_storage), "add", "Remove me"])
    result = runner.invoke(cli, ["--file", str(tmp_storage), "delete", "1"])
    assert result.exit_code == 0
    assert "deleted" in result.output.lower()
