# 문자열을 각각의 문자마다 순회하며 이전과 달라지는지 비교
# 달라지는 경우 각 알파벳마다 달라지는 횟수를 저장
# 횟수가 2 이상 알파벳이 있을 경우 그룹 단어가 아님

from collections import Counter

n = int(input())
counter = 0
for _ in range(n):
    word = input()

    group_word = Counter() # 처음 출현 횟수는 반드시 0부터 시작
    prev_char = None
    for char in word:
        if char != prev_char:
            prev_char = char
            group_word[char] += 1

    # 가장 많이 나온 알파벳 변동의 횟수가 1 이하여야지만 그룹 단어
    if group_word.most_common(1)[0][1] <= 1:
        counter += 1

print(counter)