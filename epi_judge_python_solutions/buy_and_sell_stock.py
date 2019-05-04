from test_framework import generic_test

"""Greedy algorithm that uses the min price so far to calculate the greatest
difference

Attempt Log:
- 5/2 10/10 14 minutes Got first try and can explain in an interview
"""

def buy_and_sell_stock_once(prices):

    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


def buy_and_sell_stock_once_v2(prices):
    max_profit = float("-inf")
    min_seen_so_far = float("inf")
    for p in prices:
        min_seen_so_far = min(p, min_seen_so_far)
        max_profit = max(p - min_seen_so_far, max_profit)
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
