prices = [7,1,5,3,8,4]

def maxProfit(arr):
    buy = prices[0]
    max_profit = 0

    for i in range(1, len(arr)):
        if buy > arr[i]:
            buy = arr[i]
        elif (arr[i] - buy > max_profit):
            max_profit = arr[i] - buy
        
    return max_profit

max_profit = maxProfit(prices)
print(max_profit)


#Declare a buy variable to store the min stock price encountered so far and max_profit to store the maximum profit.
#Initialize the buy variable to the first element of the prices array.
#Iterate over the prices array and check if the current price is less than buy price or not.
    #If the current price is smaller than buy price, then buy on this ith day.
    #If the current price is greater than buy price, then make profit from it and maximize the max_profit.
#Finally, return the max_profit.