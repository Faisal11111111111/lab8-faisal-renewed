from adventure.utils import read_events_from_file
import random
from rich import print
from rich.prompt import Prompt

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file("events.txt")

    print("[bold cyan]You wake up in a dark forest.[/bold cyan]")
    print("[green]You can go left or right.[/green]")

    while True:
        choice = Prompt.ask(
        "[bold yellow]Which direction do you choose?[/bold yellow]",
        choices=["left", "right", "exit"],
        default="exit"
    ).strip().lower()


        if choice == "exit":
            print("\n[bold green]Thanks for playing! You leave the forest safely. Goodbye 👋[/bold green]\n")
            break

        # Step returns plain text → tests still pass
        result = step(choice, events)

        # We only format the display, NOT the returned string
        print(f"[magenta]{result}[/magenta]")
