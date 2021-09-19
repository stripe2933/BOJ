from itertools import takewhile, repeat

n = int(input())

# Legendre's theorem
# https://jjycjnmath.tistory.com/532
#
# v2(n!)와 v5(n!)을 구하고, 그 중 최소값이 0의 개수

def get_vp(n, p):
    power = 1
    # power에 계속 p를 곱해가며 n // power를 계산, n // power가 0이 될 때까지 수 생성 후 합 계산
    return sum(takewhile(lambda x: x != 0, (n // (power := power * p) for _ in repeat(None))))

count = min(get_vp(n, 2), get_vp(n, 5))
print(count)