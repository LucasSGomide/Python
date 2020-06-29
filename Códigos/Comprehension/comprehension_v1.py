# x = [expressão for item in list if condicional]
# List Comprehension
A = [i * 2 for i in range(10)]

print(A)

# Metodo tradicional

B = []
i = 0

while i < 10:
    B.append(i * 2)
    i = i + 1
print(B)


# 2º Método tradicional

C = []

for i in range(10):
    C.append(i * 2)

print(C)
