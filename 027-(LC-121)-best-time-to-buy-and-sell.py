def best_time_to_buy_and_sell(prices):
    # Brute Force Approach
    max_profit = 0
    n = len(prices)
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if prices[j] - prices[i] > 0:
    #             profit = prices[j] - prices[i]
    #             max_profit = max(max_profit, profit)
    # return max_profit
    
    # Optimal Approach
    # hash_map = {}
    # min_price = prices[0]
    # for i in range(n):
    #     hash_map[prices[i]] = 1
    #     if prices[i] < min_price:
    #         min_price = prices[i]
    #     else:
    #         profit = prices[i] - min_price
    #         max_profit = max(max_profit, profit)
    
    # Optimal Approach
    min_price = float('inf')
    for i in range(0, n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)    
    return max_profit
    
prices = [7,1,5,3,6,5]
print(best_time_to_buy_and_sell(prices))  # Output: 5