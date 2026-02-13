#!/usr/bin/env python3
"""Interactive driver for bogosort - prompts user for numbers until 'exit' is entered."""

import sys

from bogosort import bogo_llm


def get_numbers_from_user() -> list[float]:
    """Prompt user for numbers until 'exit' is entered."""
    numbers: list[float] = []

    print("Enter numbers to sort (type 'exit' to finish):")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            break

        try:
            number = float(user_input)
            numbers.append(number)
            print(f"Added: {number}")
        except ValueError:
            print(f"Invalid input: '{user_input}'. Please enter a number or 'exit'.")

    return numbers


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
