#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for Letter in range(ord('a'), ord('z') + 1):
    print(F"{chr(Letter)}", end="")
