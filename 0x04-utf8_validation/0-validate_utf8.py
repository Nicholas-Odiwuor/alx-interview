#!/usr/bin/python3
"""
0-validate_utf8.py
UTF-8 validation routine.
"""

def validUTF8(data):
    """
    data: List[int], each int is a byte (0–255)
    Returns True if data is valid UTF-8, else False
    """
    n_bytes = 0

    for byte in data:
        # only look at the least significant 8 bits
        b = byte & 0xFF  

        if n_bytes == 0:
            # count the number of leading 1s
            mask = 0x80  # 1000 0000
            while mask & b:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                # 1-byte character
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # must be a continuation byte: starts with '10'
            if not (b & 0xC0 == 0x80):  # 1100 0000 & b should be 1000 0000
                return False

        # we have processed one byte of this multi-byte character
        n_bytes = max(n_bytes - 1, 0)

    # all characters must be fully closed
    return n_bytes == 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./0-validate_utf8.py <data_file>")
        sys.exit(1)

    # Read integers from file
    with open(sys.argv[1], 'r') as f:
        data = [int(x) for x in f.read().split()]

    print(validUTF8(data))

