"""Simple command-line calculator supporting basic arithmetic operations."""

from __future__ import annotations

import argparse
import operator
from typing import Callable, Dict, Iterable, List

Operation = Callable[[float, float], float]


def build_parser() -> argparse.ArgumentParser:
    """Create an argument parser for the calculator CLI."""
    parser = argparse.ArgumentParser(
        description="Perform basic arithmetic on a sequence of numbers."
    )
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The arithmetic operation to perform.",
    )
    parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Numbers to use in the calculation (at least two).",
    )
    return parser


def calculate(operation: str, numbers: Iterable[float]) -> float:
    """Compute the result of applying *operation* to *numbers*.

    Parameters
    ----------
    operation:
        Name of the arithmetic operation.
    numbers:
        Iterable of numbers to use. Must contain at least two elements.
    """
    num_list: List[float] = list(numbers)
    if len(num_list) < 2:
        raise ValueError("At least two numbers are required for calculation.")

    operations: Dict[str, Operation] = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv,
    }

    op = operations[operation]

    result = num_list[0]
    for value in num_list[1:]:
        if operation == "divide" and value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = op(result, value)
    return result


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = calculate(args.operation, args.numbers)
    except (ValueError, ZeroDivisionError) as exc:
        parser.error(str(exc))
    print(result)


if __name__ == "__main__":
    main()
