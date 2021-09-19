from sys import stdin, stdout

t = int(stdin.readline())
for query in (stdin.readline().strip() for _ in range(t)):
    stack = []
    flag = True # True - VPS, False - 무효한 PS

    for char in query:
        if char == '(':
            stack.append(char)
        else: # char == ')'
            if len(stack) == 0: # 무효한 PS
                flag = False
                break
            stack.pop()
    
    if len(stack) != 0: # 무효한 PS
        flag = False
    
    stdout.write('YES\n' if flag else 'NO\n')

stdout.flush()