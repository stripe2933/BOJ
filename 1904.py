n = int(input())

fibonacci = [1, 2]

for _ in range(n - 2):
    fibonacci.append((fibonacci[-1] + fibonacci[-2]) % 15746)

print(fibonacci[-1] if n >= 3 else n)