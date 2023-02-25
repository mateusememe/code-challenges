a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

values = [a, b, c, d, e]

count_pairs = 0

for value in values:
    count_pairs += 1 if value % 2 == 0 else 0

print(f'{count_pairs} valores pares\n')
