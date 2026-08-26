import click

from cli_task_manager_sln.storage import TaskStorage
from cli_task_manager_sln.task import Task


@click.group()
@click.option(
    "--file",
    default="tasks.json",
    help="Path to the tasks file",
)
@click.pass_context
def cli(ctx, file):
    """Task Manager CLI."""
    ctx.ensure_object(dict)

    try:
        ctx.obj["storage"] = TaskStorage(file)
    except ValueError as error:
        raise click.ClickException(str(error)) from error


@cli.command()
@click.argument("description")
@click.option(
    "--priority",
    type=click.Choice(["low", "normal", "high"]),
    default="normal",
    show_default=True,
)
@click.pass_context
def add(ctx, description, priority):
    """Add a new task."""
    storage = ctx.obj["storage"]

    try:
        new_task = Task(
            id=storage._get_next_id(),
            description=description,
            completed=False,
            priority=priority,
        )
        storage.add(new_task)
    except ValueError as error:
        raise click.ClickException(str(error)) from error

    click.echo(f"Task added: ID {new_task.id}")


@cli.command(name="list")
@click.pass_context
def list_tasks(ctx):
    """List all tasks."""
    storage = ctx.obj["storage"]
    tasks = storage.get_all()

    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo("ID | Status | Description | Priority")
    click.echo("---+--------+-------------+---------")

    for task in tasks:
        status = "[x]" if task.completed else "[ ]"

        click.echo(
            f"{task.id} | {status} | "
            f"{task.description} | "
            f"{task.priority.capitalize()}"
        )


@cli.command()
@click.argument("task_id", type=int)
@click.pass_context
def done(ctx, task_id):
    """Mark a task as complete."""
    storage = ctx.obj["storage"]
    task = storage.get_by_id(task_id)

    if task is None:
        raise click.ClickException(f"Task {task_id} not found.")

    task.completed = True
    storage.save()

    click.echo(f"Task {task_id} marked as complete")


@cli.command()
@click.argument("task_id", type=int)
@click.pass_context
def delete(ctx, task_id):
    """Delete a task."""
    storage = ctx.obj["storage"]

    if not storage.delete(task_id):
        raise click.ClickException(f"Task {task_id} not found.")

    click.echo(f"Task {task_id} deleted")
