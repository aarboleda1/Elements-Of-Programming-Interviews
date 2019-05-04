from test_framework import generic_test

"""
Attempt Log

- 5/3/19 0/10, didn't understand question. We need to know what buys and sells
happened on day 1. So, we keep an extra data structure and cache the max_profit
that could have taken place at each index.

The 2nd step is to work backwards. LOOK ON LEETCODE, not sure about the solution
in EPI and this still needs work
"""
def buy_and_sell_stock_twice(prices):

    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    # Forward phase. For each day, we record maximum profit if we sell on that
    # day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit
    print(first_buy_sell_profits)
    # Backward phase. For each day, find the maximum profit if we make the
    # second buy on that day.
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_sell_profits[i - 1])
    return max_total_profit


def buy_and_sell_stock_twice_constant_space(prices):
    min_prices, max_profits = [float('inf')] * 2, [0] * 2
    for price in prices:
        for i in reversed(list(range(2))):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i],
                                price - (0 if i == 0 else max_profits[i - 1]))
    return max_profits[-1]


if __name__ == '__main__':
    buy_and_sell_stock_twice([100, 20, 90, 0, 20])
    # exit(
    #     generic_test.generic_test_main("buy_and_sell_stock_twice.py",
    #                                    "buy_and_sell_stock_twice.tsv",
    #                                    buy_and_sell_stock_twice))
