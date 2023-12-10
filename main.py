from typing import Annotated
import typer

from src import (Download, WhipeSD)

app = typer.Typer()


@app.command()
def download(mode: str):
    try:
        Download(mode).execute()
    except Exception as e:
        typer.echo(e)
        typer.Exit()

@app.command()
def delete(
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete ALL medias?")
    ]):
    if force:
        try:
            WhipeSD().execute()
        except Exception as e:
            typer.echo(e)
            typer.Exit()
    else:
        typer.echo('Operation cancelled')


if __name__ == '__main__':
    app()
