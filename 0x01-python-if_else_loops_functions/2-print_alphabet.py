#!/usr/bin/python3
"""
Print the ASCII alphabet in lowercase, not followed by a new line.
"""
for Lette in range(ord('A'), ord('Z') + 1):
    print(F"{chr(Lette)} = {Lette} \t\t {chr(Lette)} = {Lette}\n", end="")
