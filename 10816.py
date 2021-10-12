from bisect import bisect_left, bisect_right
from sys import stdout

n = int(input())
nums = sorted(map(int, input().split()))
m = int(input())

for query in map(int, input().split()):
    stdout.write(f'{bisect_right(nums, query) - bisect_left(nums, query)} ')
    
stdout.flush()