#!/usr/bin/python3
def makeChange(coins, total):
    previous_amounts = {}

    def coinChangeHelper(coins, amount, previous_amounts):
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
            return -1

    return coinChangeHelper(coins, total, previous_amounts)

# print(makeChange([1, 2, 25], 37))

# print(makeChange([1256, 54, 48, 16, 102], 1453))