from invoke import task


@task
def foo(ctx):
    print("bar")


@task
def start(ctx):
    ctx.run("python src/run_program.py", pty=True)  # pty = True)


@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)


@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)


@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
