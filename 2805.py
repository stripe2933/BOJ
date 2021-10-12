n, m = map(int, input().split())
heights = list(map(int, input().split()))

left, right = 0, 1000000000
while left <= right:
    mid = (left + right) // 2
    heights_sum = sum(h - mid for h in heights if h > mid)
    
    if heights_sum >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)