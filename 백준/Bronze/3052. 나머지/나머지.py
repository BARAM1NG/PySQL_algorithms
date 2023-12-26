numbers = []
numbers2 = []

for _ in range(10):
  A = int(input())
  numbers.append(A)

for i in numbers:
  B = i % 42
  numbers2.append(B)

print(len(set(numbers2)))