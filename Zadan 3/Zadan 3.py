n = int(input("Введите число: "))

temp = 0
result = 0

while result * 2 < n:
    result = 2**temp
    print(result)
    temp += 1