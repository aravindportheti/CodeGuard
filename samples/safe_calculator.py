"""
Safe Calculator Module
Demonstrates clean, PEP 8 compliant, secure Python code without vulnerabilities.
"""

from typing import Union, List

Number = Union[int, float]

class SafeCalculator:
    """A secure, type-safe mathematical utility class."""

    def __init__(self, precision: int = 2):
        self.precision = precision
        self.history: List[str] = []

    def add(self, a: Number, b: Number) -> Number:
        """Computes the sum of two numbers."""
        res = round(a + b, self.precision)
        self.history.append(f"{a} + {b} = {res}")
        return res

    def subtract(self, a: Number, b: Number) -> Number:
        """Computes the difference of two numbers."""
        res = round(a - b, self.precision)
        self.history.append(f"{a} - {b} = {res}")
        return res

    def multiply(self, a: Number, b: Number) -> Number:
        """Computes the product of two numbers."""
        res = round(a * b, self.precision)
        self.history.append(f"{a} * {b} = {res}")
        return res

    def divide(self, a: Number, b: Number) -> Number:
        """Computes the quotient of two numbers with zero-division validation."""
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        res = round(a / b, self.precision)
        self.history.append(f"{a} / {b} = {res}")
        return res


def run_demo():
    calc = SafeCalculator(precision=3)
    val1 = calc.add(10.5, 4.25)
    val2 = calc.multiply(val1, 2)
    print(f"Calculated result: {val2}")

if __name__ == "__main__":
    run_demo()
