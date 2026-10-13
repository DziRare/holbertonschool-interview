#!/usr/bin/python3
"""Min operations module"""


def minOperations(n):
    """This is for min operations"""
    if n <= 1:
        return 0
    if n == 2:
        return 2

    if n % 2 == 0:
        return 2 + minOperations(n // 2)
    else:
        for i in range(n):
            if i * n == n:
                return 1 + minOperations(i)


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
