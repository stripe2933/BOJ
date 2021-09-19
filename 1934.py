from math import gcd

# A * B = gcd(A, B) * lcm(A, B)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))