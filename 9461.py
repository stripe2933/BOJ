from functools import cache

@cache
def padoban(n):
    if n <= 5:
        return (n + 2) // 3
    
    return padoban(n - 1) + padoban(n - 5)

t = int(input())
for n in (int(input()) for _ in range(t)):
    print(padoban(n))