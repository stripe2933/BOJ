from sys import stdin, stdout
from bisect import insort

n = int(stdin.readline())
nums = []

for _ in range(n):
    insort(nums, int(stdin.readline()))
    stdout.write(f'{nums[(len(nums) - 1) // 2]}\n')
stdout.flush()