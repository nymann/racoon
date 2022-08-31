import typer

app = typer.Typer()


@app.command()
def generate() -> None:
    typer.echo("TBD")


if __name__ == "__main__":
    app()
