bin(5)[2:].zfill(8)  # Output: '00000101'


def pad_binary_string(binary_str: str, length: int) -> str:
    """Pad a binary string with leading zeros to a specified length."""
    return binary_str.zfill(length) # Pad with leading zeros    
# Example usage
if __name__ == "__main__":     
    binary_str = "101"
    padded_str = pad_binary_string(binary_str, 8)
    print(padded_str)  # Output: '00000101'
    
    # Example with a different length
    padded_str = pad_binary_string(binary_str, 12)
    print(padded_str)  # Output: '00000000101'
# Output: '0000000101'  
# Output: '00000000101'