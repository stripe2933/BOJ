from sys import stdout

a, b = map(int, input().split())
if b >= 10000000: # 10000000~100000000 까지는 palindrome이 없음
    b = 9999999

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
    a_list = (2, 7, 61,)

    if n < 2:
        return False
    elif n in a_list:
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
        return True
    
    return False

for num in range(a, b + 1):
    num_str = str(num)
    if num_str != num_str[::-1]: # palindrome 검사
        continue

    if num % 2 == 0: # 짝수인 경우 제외
        continue

    if miller_rabin(num): # 소수 판별
        stdout.write(f'{num}\n')

stdout.write('-1\n')
stdout.flush()