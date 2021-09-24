from math import inf

n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[triangle[0][0]]]
for i in range(1, n):
    dp.append(
        [triangle[i][j] + max(dp[-1][j-1] if j != 0 else -inf, dp[-1][j] if j != i else -inf) for j in range(i + 1)]
    )

print(max(dp[-1]))