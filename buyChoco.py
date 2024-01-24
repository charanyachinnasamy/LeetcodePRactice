def buyChoco(prices,money):
    prices.sort()
    cost = prices[0]+prices[1]
    if cost>money:
        return money
    else:
        return money-cost

print(buyChoco([1,1],100))
