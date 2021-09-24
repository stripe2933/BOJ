n, r, c = map(int, input().split())

begin, end = 0, 2 ** (2 * n)
left, right, top, bottom = 0, 2 ** n, 0, 2 ** n

while begin + 1 != end:
    horizontal_mid = (left + right) // 2
    vertical_mid = (top + bottom) // 2

    if r < vertical_mid:
        if c < horizontal_mid:
            end = (3 * begin + end) // 4
            right = horizontal_mid
        else:
            begin, end = (3 * begin + end) // 4, (begin + end) // 2
            left = horizontal_mid
        bottom = vertical_mid
    else:
        if c < horizontal_mid:
            begin, end = (begin + end) // 2, (begin + 3 * end) // 4
            right = horizontal_mid
        else:
            begin = (begin + 3 * end) // 4
            left = horizontal_mid
        top = vertical_mid

print(begin)