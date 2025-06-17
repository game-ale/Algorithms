dp = [False] * (target + 1)
dp[0] = True
for num in nums:
    for j in range(target, num - 1, -1):
        dp[j] |= dp[j - num]
