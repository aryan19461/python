def coin_permu(coin , sum , ans ):
    if(sum == 0):
        print(ans)
        return
    
    for i in range(len(coin)):
        if(coin[i] <= sum):
            coin_permu(coin,sum-coin[i],ans+" "+str(coin[i]) )
            

coin = [2,4,7,8,9,10,12]
coin_permu(coin,20,"")
'''
In this Python code, coin is a list of integers representing the available coins, total is the target sum, and ans is a string representing the current combination of coins being considered.

The coin_permu function is a recursive function that generates all possible combinations of coins that add up to the target sum. If the target sum has been reached, it prints the current combination and returns. Otherwise, it loops through each available coin and recursively tries to generate combinations that add up to the remaining sum. When the recursive call returns, it removes the coin from the combination to backtrack and try another coin.

The example usage at the end of the code creates a list of coins and a target sum, and calls the coin_permu function with the coins, the target sum, and an empty string representing the current combination of coins.
'''