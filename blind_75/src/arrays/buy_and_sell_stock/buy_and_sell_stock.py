def max_profit(prices):
    left, right = 0, 1 #left represents when to buy and right represnts when to sell
    max_profit = 0
    
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        
        right += 1
    
    return max_profit
    

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))