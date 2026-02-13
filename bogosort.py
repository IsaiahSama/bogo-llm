# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "openai>=1.0.0",
#     "python-dotenv>=1.0.0",
# ]
# ///

import argparse
import os
import re

from dotenv import load_dotenv
from openai import OpenAI

_ = load_dotenv()

DEFAULT_MODEL = os.getenv("MODEL_NAME", "local-model")
DEFAULT_API_URL = os.getenv("API_URL", "http://localhost:1234/v1")
DEFAULT_API_KEY = os.getenv("API_KEY", "not-needed")


def bogo_llm(
    numbers: list[float],
    model_name: str = DEFAULT_MODEL,
    api_url: str = DEFAULT_API_URL,
) -> str:
    client = OpenAI(base_url=api_url, api_key=DEFAULT_API_KEY)

    numbers_str = ", ".join(map(str, numbers))
    prompt = f"Sort the following list of numbers and return ONLY the sorted list in bracket notation like this: [num1, num2, num3]. Do not add any other text. Here is the list: [{numbers_str}]"

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )

    content = response.choices[0].message.content
    if content:
        content = content.strip()
    else:
        return "I honestly have no idea! Get Bogo'd!"

    # Try to extract the list from the response
    match = re.search(r"\[([^\]]+)\]", content)
    if match:
        sorted_list_str = match.group(0)
        return f"The sorted list is {sorted_list_str}"
    else:
        return f"The sorted list is [{content}]"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort numbers using a local LLM via LM Studio"
    )
    _ = parser.add_argument(
        "numbers", nargs="+", type=float, help="list of numbers to sort"
    )
    _ = parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model name (default: {DEFAULT_MODEL})",
    )
    _ = parser.add_argument(
        "--url",
        default=DEFAULT_API_URL,
        help=f"LM Studio API URL (default: {DEFAULT_API_URL})",
    )

    args = parser.parse_args()

    result = bogo_llm(args.numbers, args.model, args.url)  # pyright: ignore[reportAny]
    print(result)


if __name__ == "__main__":
    main()
