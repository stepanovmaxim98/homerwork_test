# Урок №4. Float, int и арифмитические операции
# Задание №1
a = float(input())
b = float(input())
print(a * b)
print((a + b) * 2)
# Задание №2
c = int(input())
result = []
for i in str(c):
    result.append(int(i))
n = result[3] ** result[4]
v = (n * result[2]) / (result[0] - result[1])
print(v)

