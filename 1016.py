from math import ceil, sqrt
from operator import truth

minimum, maximum = map(int, input().split())

# [minimum, maximum] 구간의 수를 소인수분해했을 경우
# 최대 소인수는 int(sqrt(maximum))을 넘지 않음

bound = int(sqrt(maximum)) + 1
sieve = [True] * bound
sieve[0] = 0
sieve[1] = 0
for i in range(3, int(sqrt(bound)) + 1, 2):
    if sieve[i]:
        sieve[i**2::2*i] = [False] * ((bound - i**2 - 1) // (2*i) + 1)

primes = (idx for idx, is_prime in enumerate(sieve) if is_prime)

square_free = [True] * (maximum - minimum + 1)
for prime in primes:
    prime_square = prime ** 2

    # prime_square의 배수는 모두 square-free가 아님
    for i in range((prime_square - minimum % prime_square) % prime_square, len(square_free), prime_square):
        square_free[i] = False

print(sum(filter(truth, square_free)))