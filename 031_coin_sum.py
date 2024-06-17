def coin_sum(coins, sum, n, dp):
    if sum == 0:
        dp[n][sum] = 1
        return dp[n][sum]

    if sum < 0 or n <= 0:
        return 0

    if dp[n][sum] != -1:
        return dp[n][sum]

    return coin_sum(coins, sum - coins[n-1], n, dp) + coin_sum(coins, sum, n - 1, dp)


sum = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [[-1 for i in range(sum+1)] for j in range(len(coins)+1)]
print(coin_sum(coins, sum, len(coins), dp))
# print(len(dp[0]))
