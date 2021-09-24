from sys import stdin
from operator import truth

# 면적을 A라 하면
# A = 2xy + x + y
# 2A + 1 = 4xy + 2x + 2y + 1 = (2x + 1)(2y + 1)
#
# 즉, 2A + 1이 합성수여야만 유효 면적이 될 수 있음

def fast_pow(a, p, mod):
    if p == 0:
        return 1 % mod
    elif p == 1:
        return a % mod
    
    power_div_square = fast_pow(a, p // 2, mod) ** 2
    if p % 2 == 0:
        return power_div_square % mod
    else:
        return (power_div_square * a) % mod

def miller_rabin(n):
    # n이 1373653 미만일 경우 a = 2, 3 만 검사하여도 충분
    a_list = (2, 3,)

    # 인자의 n이 언제나 2 이상만 들어오므로 그 이하 경우에 대한 예외 처리 제외
    if n in a_list:
        return True

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for a in a_list:
        a_power = fast_pow(a, d, n)
        if a_power == 1:
            continue

        for r in range(s):
            if a_power == n - 1:
                break

            a_power = (a_power ** 2) % n
        else: # none of above
            break
    else:
        return True # prime
    
    return False # not prime

n = int(stdin.readline())
count = sum(filter(truth, (miller_rabin(2 * int(stdin.readline()) + 1) for _ in range(n))))
print(count)