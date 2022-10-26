#!/usr/bin/env/python3

# islower - function that check for lowercase character
# Return - True ifEquals lowercase, if otherwise False

def islower(c):
    if (ord(c) > 96 and ord(c) <= 122):
        return True
    else:
        False
