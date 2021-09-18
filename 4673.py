from sys import stdout

sieve = [False] * 10001 # 초기에는 모두 생성자가 없는 것으로 간주

def self_number(n):
    return n + sum(map(int, str(n)))

for n in range(1, 10001):
    if not sieve[n]: # False일 경우 생성자가 없는 상태
        stdout.write(f'{n}\n')
        
        while (n := self_number(n)) <= 10000: # d(n)
            sieve[n] = True

stdout.flush()