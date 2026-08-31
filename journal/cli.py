import click
from datetime import date

from .db import get_entries, init_db, insert_entry
from .models import Entry


@click.group()
def cli():
    """A habit-focused daily journal covering relationships, learning, money, and health."""
    init_db()


@cli.command()
def add():
    """Add today's journal entry."""
    click.echo("\n-- Relationships --")
    rel_note = click.prompt("Note")
    rel_rating = click.prompt("Rating (1-5)", type=click.IntRange(1, 5))

    click.echo("\n-- Learning --")
    learn_note = click.prompt("Note")
    learn_minutes = click.prompt("Minutes spent", type=int)

    click.echo("\n-- Money --")
    money_note = click.prompt("Note")
    money_spent = click.prompt("Amount spent today", type=float)

    click.echo("\n-- Health --")
    health_note = click.prompt("Note")
    sleep_hours = click.prompt("Hours slept", type=float)
    exercised = click.confirm("Did you exercise?")

    entry = Entry(
        entry_date=date.today(),
        relationships_note=rel_note,
        relationships_rating=rel_rating,
        learning_note=learn_note,
        learning_minutes=learn_minutes,
        money_note=money_note,
        money_spent=money_spent,
        health_note=health_note,
        sleep_hours=sleep_hours,
        exercised=exercised,
    )
    insert_entry(entry)

    click.echo(f"\n✓ Entry saved for {entry.entry_date.isoformat()}")


@cli.command(name="list")
@click.option("--limit", default=7, help="Number of entries to show")
def list_entries(limit):
    """Show recent entries."""
    entries = get_entries(limit)

    if not entries:
        click.echo("No entries yet. Run 'journal add' to create one.")
        return

    for entry in entries:
        click.echo(f"\n{entry.entry_date.isoformat()}")
        click.echo(f"  Relationships: {entry.relationships_note} (rated {entry.relationships_rating}/5)")
        click.echo(f"  Learning: {entry.learning_note} ({entry.learning_minutes} min)")
        click.echo(f"  Money: {entry.money_note} (${entry.money_spent:.2f})")
        click.echo(f"  Health: {entry.health_note} (slept {entry.sleep_hours}h, exercised: {entry.exercised})")


if __name__ == "__main__":
    cli()
