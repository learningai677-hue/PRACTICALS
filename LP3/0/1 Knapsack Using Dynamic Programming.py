
# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for j in range(capacity + 1)]
          for i in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
capacity = 5

max_profit = knapsack(weights, profits, capacity)

print("Maximum Profit:", max_profit)
