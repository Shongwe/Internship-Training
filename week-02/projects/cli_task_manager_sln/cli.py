import click
from cli_task_manager_sln.storage import TaskStorage
from cli_task_manager_sln.task import Task

@click.group()
@click.option('--file', default='tasks.json', help='Path to the tasks file')
@click.pass_context
def cli(ctx, file):
    ctx.ensure_object(dict)
    ctx.obj['storage'] = TaskStorage(file)

@cli.command()
@click.argument('task')
@click.pass_context
def add(ctx, task):
    storage = ctx.obj['storage']
    new_task = Task(id=storage._get_next_id(), description=task, completed=False)
    storage.add(new_task)
    click.echo(f"Task added: {task}")

@cli.command(name="list")
@click.pass_context
def list_tasks(ctx):
    storage = ctx.obj['storage']
    tasks = storage.get_all()
    if not tasks:
        click.echo("No tasks found.")
        return
    for t in tasks:
        status = "✓" if t.completed else "✗"
        click.echo(f"{t.id}. [{status}] {t.description}")

@cli.command()
@click.argument('task_id', type=int)
@click.pass_context
def done(ctx, task_id):
    storage = ctx.obj['storage']
    for t in storage.get_all():
        if t.id == task_id:
            t.completed = True
            storage.save()
            click.echo(f"Task {task_id} marked as complete")
            return
    click.echo("Invalid task ID")

@cli.command()
@click.argument('task_id', type=int)
@click.pass_context
def delete(ctx, task_id):
    storage = ctx.obj['storage']
    before = len(storage.get_all())
    storage.delete(task_id)
    after = len(storage.get_all())
    if after < before:
        click.echo(f"Task {task_id} deleted")
    else:
        click.echo("Invalid task ID")
