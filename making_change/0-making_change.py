#!/usr/bin/python3
"""
Main file for runing mak change
"""

def makeChange(coins, total):
    """
    Main function for running make change
    """
    previous_amounts = {}

    def coinChangeHelper(coins, amount, previous_amounts):
        """
        Helper function for running make change
        """
        if amount == 0:
            return 0
        if amount in previous_amounts:
            return previous_amounts[amount]

        counts = []
        for coin in coins:
            if coin <= amount:
                sub_count = coinChangeHelper(coins, amount - coin, previous_amounts)
                if sub_count > -1:
                    counts.append(sub_count + 1)

        if counts:
            previous_amounts[amount] = min(counts)
            return min(counts)
        else:
            previous_amounts[amount] = -1
            return -1

    return coinChangeHelper(coins, total, previous_amounts)

# print(makeChange([1, 2, 25], 37))

# print(makeChange([1256, 54, 48, 16, 102], 1453))