from sys import stdin, stdout
from heapq import heappush, heappop

n = int(stdin.readline())
heap = []
for _ in range(n):
    command = int(stdin.readline())
    if command == 0:
        stdout.write(f'{heappop(heap)[1] if heap else 0}\n')
    else:
        heappush(heap, (abs(command), command))
stdout.flush()