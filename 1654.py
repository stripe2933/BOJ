from sys import stdin

k, n = map(int, stdin.readline().split())
lengths = [int(stdin.readline()) for _ in range(k)]

left, right = 1, 2**31-1
while left <= right:
    mid = (left + right) // 2

    count = sum(length // mid for length in lengths)
    if count < n:
        right = mid - 1
    else:
        left = mid + 1

print(right)