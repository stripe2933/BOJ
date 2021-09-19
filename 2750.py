from sys import stdin, stdout

n = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(n)]

nums.sort()

for num in nums:
    stdout.write(f'{num}\n')
stdout.flush()