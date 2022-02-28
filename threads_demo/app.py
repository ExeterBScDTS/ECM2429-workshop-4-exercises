"""An example of launching threads.
"""


def print_help() -> None:
    """Print a help message.
    """
    print("Enter one of the following commands:")
    print("\thelp\tdisplays this message")
    print("\ttick [interval=1]\tstart a tick-tock daemon")
    print("\tcount [end=10] [rate=1][\tstart a countdown")
    print("\tquit\tquit when all countdowns have completed")
    print()


def print_unknown(command: str) -> None:
    """Prompts user to enter help if they attempt and unknown command.

    :param command: the unknown command
    :type command: str
    """
    print(f"The command '{command}' is not recognised.")
    print("Enter 'help' to see a list of recognised commands.")
    print()


def do_tick(args) -> None:
    """
    """
    delay = 1.0
    if len(args) > 0:
        delay = float(args[0])
    print(f"tick-tock with interval {delay} starting...")
    pass


def do_count(args) -> None:
    """
    """
    end = 10.0
    rate = 1.0
    if len(args) > 0:
        end = float(args[0])
    if len(args) > 1:
        rate = float(args[1])
    print(f"countdown to {end} (rate {rate}) starting...")
    pass


def mainloop():
    """An even-loop that takes a typed command using the input() statement.
    """
    while True:
        # Wait here until the user types a command
        input_text = input("enter a command > ")

        args = input_text.split()
        command = args[0]
        args = args[1:]

        if command == "help":
            print_help()
        # Can match the command to one of several words using 'in'
        elif command in ("quit", "exit"):
            break
        elif command == "tick":
            do_tick(args)
        elif command == "count":
            do_count(args)
        else:
            print_unknown(command)


if __name__ == "__main__":
    mainloop()
    print("Goodbye")
