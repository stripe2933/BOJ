sieve = [True] * (1000 + 1) # 처음에는 모든 수가 소수라고 가정

sieve[0] = False
sieve[1] = False
for i in range(2, 1000 + 1):
    if not sieve[i]: # 합성수인 경우 순회 재개
        continue

    # 해당 수 제외한 그 배수는 모두 소수 처리
    for j in range(2 * i, 1000 + 1, i):
        sieve[j] = False

primes = set(i for i, is_prime in enumerate(sieve) if is_prime)

n = int(input())

counter = 0
for num in map(int, input().split()):
    if num in primes:
        counter += 1

print(counter)