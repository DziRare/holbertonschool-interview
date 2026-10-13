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
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return (n // i) + minOperations(i)
