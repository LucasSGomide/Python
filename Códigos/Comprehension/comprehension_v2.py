# x = [expressão for item in list if condicional]
# List Comprehension
A = [i * 2 for i in range(10) if i % 2 == 0]

print(A)

# Metodo tradicional

B = []

for i in range(10):
    if i % 2 == 0:
        B.append(i * 2)

print(B)
