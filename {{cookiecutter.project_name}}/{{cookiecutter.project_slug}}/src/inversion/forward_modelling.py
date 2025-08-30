# src/example_project/mymodule.py

class Calculator:
    """
    A simple calculator class.

    Methods:
        add(a, b): Return the sum of a and b.
        multiply(a, b): Return the product of a and b.
    """

    def add(self, a: int, b: int) -> int:
        """Return the sum of a and b."""
        return a + b

    def multiply(self, a: int, b: int) -> int:
        """Return the product of a and b."""
        return a * b
