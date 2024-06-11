def coin_sum(coins,sum,i,dp):
    if sum==0:
        dp[i][sum] = 1
        return dp[i][sum]
    
    if sum < 0 or i <= 0:
        return 0
    
    if dp[i][sum] != -1:
        return dp[i][sum]
    
    return coin_sum(coins,sum-coins[i],i,dp) + coin_sum(coins,sum,i-1,dp)

sum = 200
coins = [1,2,5,10,20,50,100,200]
dp = [[-1 for i in range(sum)] for j in range(len(coins))]
print(coin_sum(coins,sum,len(coins)-1,dp))
# print(len(dp[0]))