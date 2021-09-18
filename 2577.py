from collections import Counter

a, b, c = map(int, (input() for _ in range(3)))
multiply = a * b * c

counter = Counter(str(multiply))
for i in range(10):
    print(counter.get(str(i), 0))