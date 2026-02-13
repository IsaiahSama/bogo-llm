#!/usr/bin/env python3
"""Interactive driver for bogosort - prompts user for numbers until 'exit' is entered."""

import random
import sys

from bogosort import bogo_llm


def get_numbers_from_user() -> list[float]:
    """Prompt user for numbers until 'exit' is entered."""
    numbers: list[float] = []

    print("Enter numbers to sort (type 'exit' to finish, or 'random' for chaos):")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "random":
            numbers = generate_random_list()
            print(f"Generated {len(numbers)} random numbers: {numbers}")
            break

        try:
            number = float(user_input)
            numbers.append(number)
            print(f"Added: {number}")
        except ValueError:
            print(
                f"Invalid input: '{user_input}'. Please enter a number, 'random', or 'exit'."
            )

    return numbers


def generate_random_list() -> list[float]:
    """Generate a list of 10-30 random numbers between -100 and 100."""
    count = random.randint(10, 30)
    return [round(random.uniform(-100, 100), 2) for _ in range(count)]


def main() -> None:
    """Main entry point for the interactive driver."""
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered. Exiting.")
        sys.exit(0)

    print(f"\nSorting {len(numbers)} number(s) using Bogomagic...")
    result = bogo_llm(numbers)
    print(f"\n{result}")


if __name__ == "__main__":
    main()
