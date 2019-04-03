def maxProfit(prices):
    minprice = prices[0]
    maxprice = 0
    for i in range(0, len(prices)):
        maxprice = max(maxprice, prices[i] - minprice)
        minprice = min(minprice, prices[i])
    return maxprice

maxProfit([7,1,5,3,6,4])