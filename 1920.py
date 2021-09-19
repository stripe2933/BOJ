from sys import stdout

n = int(input())
nums = set(map(int, input().split()))

m = int(input())
for query in map(int, input().split()):
    if query in nums:
        stdout.write(f'1\n')
    else:
        stdout.write(f'0\n')
stdout.flush()