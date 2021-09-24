dp = [(0, 0, 0)]

n = int(input())
for r, g, b in (map(int, input().split()) for _ in range(n)):
    dp.append((
        min(dp[-1][1], dp[-1][2]) + r,
        min(dp[-1][0], dp[-1][2]) + g,
        min(dp[-1][0], dp[-1][1]) + b,
    ))
    
print(min(dp[-1]))