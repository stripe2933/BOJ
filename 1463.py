from math import inf

n = int(input())

dp = [inf, 0]
for i in range(2, n + 1):
    min_operation = 1 + min(
        dp[i // 3] if i % 3 == 0 else inf,
        dp[i // 2] if i % 2 == 0 else inf,
        dp[i - 1]
    )
    dp.append(min_operation)

print(dp[-1])