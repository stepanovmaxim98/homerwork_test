# Урок №5. Логические и условные операторы
# Задание №1
n = int(input())
if n < 0 and n % 2 == 0:
    print('Отрицательное четное число')
elif n == 0:
    print('Нулевое число')
elif n > 0 and n % 2 != 0:
    print('Положительное нечетное число')
elif n > 0 and n % 2 == 0:
    print('Положительное четное число')
elif n < 0 and n % 2 != 0:
    print('Отрицательное нечетное число')
elif n % 2 != 0:
    print('Число не является четным')

# Задание №2
s = input()
count = 0
soglasn = 0
if 'a' or 'e' or 'i' or 'o' or 'u' in s:
    print(True)
else:
    print(False)
for i in range(len(s)):
    if s[i] in 'aeiou':
        count += 1
    if s[i] in 'bcdfghjklmnpqrstvxz':
        soglasn += 1
print(count)
print(soglasn)

# Задание №3
x = int(input('Введите минимальную сумму инвестиций: '))
Micle = int(input('Введите количество денег у Майкла: '))
Ivan = int(input('Введите количество денег у Ивана: '))
if Micle >= x and Ivan >= x:
    print(2)
if Micle >= x and Ivan < x:
    print('Micle')
if Ivan >= x and Micle < x:
    print('Ivan')
if Ivan < x and Micle < x:
    print(0)
if Ivan + Micle >= x:
    print(1)