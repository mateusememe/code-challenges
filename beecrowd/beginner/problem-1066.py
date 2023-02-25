a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

values = [a, b, c, d, e]

counts = {
  'pairs': 0,
  'odd': 0,
  'positives': 0,
  'negatives': 0
}

for value in values:
  counts['pairs'] += 1 if value % 2 == 0 else 0
  counts['odd'] += 1 if value % 2 == 1 else 0
  counts['positives'] += 1 if value > 0 else 0
  counts['negatives'] += 1 if value < 0 else 0


print(counts["pairs"], 'valor(es) par(es)')
print(counts["odd"], 'valor(es) impar(es)')
print(counts["positives"], 'valor(es) positivo(s)')
print(counts["negatives"], 'valor(es) negativo(s)')
