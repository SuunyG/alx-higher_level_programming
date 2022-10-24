#!/usr/bin/python3
for num in range(0, 9):
    for num_1 in range(1, 10):
        if num < num_1 and num != 8:
            print("{}{},".format(num, num_1), end = " ")
        elif num == 8 and num_1 == 9:
            print("{}{}".format(num, num_1))
