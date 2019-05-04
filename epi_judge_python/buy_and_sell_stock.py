from test_framework import generic_test

"""Design an algorithm that determines the maximum profit that could have been
made by buying and then selling a single share over a given day range. The buy
and sell of a stock must take place at the start of a day

stocks = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
- maximum profit is 30. Buy at 260, sell at 290

max_profit = 30
min_seen_so_far = min(A[i], min_seen_so_far)
max_profit = max(A[i] - min_seen_so_far, max_profit)

Attempt Log:
- 5/2, 14 minutes
"""


def buy_and_sell_stock_once(prices):
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
