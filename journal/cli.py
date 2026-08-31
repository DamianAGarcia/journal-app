import click
from datetime import date

from .db import get_connection, init_db


@click.group()
def cli():
    """A habit-focused daily journal covering relationships, learning, money, and health."""
    init_db()


@cli.command()
def add():
    """Add today's journal entry."""
    entry_date = date.today().isoformat()

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

    conn = get_connection()
    conn.execute("""
        INSERT OR REPLACE INTO entries VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (
        entry_date, rel_note, rel_rating, learn_note, learn_minutes,
        money_note, money_spent, health_note, sleep_hours, int(exercised)
    ))
    conn.commit()
    conn.close()

    click.echo(f"\n✓ Entry saved for {entry_date}")


@cli.command(name="list")
@click.option("--limit", default=7, help="Number of entries to show")
def list_entries(limit):
    """Show recent entries."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM entries ORDER BY entry_date DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()

    if not rows:
        click.echo("No entries yet. Run 'journal add' to create one.")
        return

    for row in rows:
        click.echo(f"\n{row[0]}")
        click.echo(f"  Relationships: {row[1]} (rated {row[2]}/5)")
        click.echo(f"  Learning: {row[3]} ({row[4]} min)")
        click.echo(f"  Money: {row[5]} (${row[6]:.2f})")
        click.echo(f"  Health: {row[7]} (slept {row[8]}h, exercised: {bool(row[9])})")


if __name__ == "__main__":
    cli()
