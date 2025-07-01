"""🔢 1. Convert Between Binary and Decimal
Task	Code
Convert int to binary string	bin(n) → '0b1010'
Get binary without '0b' prefix	bin(n)[2:]
Convert binary string to int	int('1010', 2) → 10

"""
def int_to_binary(n: int) -> str:
    """Convert an integer to a binary string."""
    return bin(n)[2:]  # Remove the '0b' prefix
def binary_to_int(binary_str: str) -> int:
    """Convert a binary string to an integer."""
    return int(binary_str, 2)

       