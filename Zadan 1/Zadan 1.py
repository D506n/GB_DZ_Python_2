import random

n = input('Введите количество монет:')

coins = []

while len(coins) < int(n):
    coins.append(random.randint(0, 1))

print(f'Монетки на столе(Орёл - 1, Решка - 0): {coins}')

step = 0
eagle_count = 0
tails_count = 0

while step < len(coins):
    if coins[step] == 1:
        eagle_count += 1
    else:
        tails_count += 1
    step += 1

print(f"""Количество орлов на столе:  {eagle_count}
Количество решек на столе: {tails_count}""")

if eagle_count > tails_count:
    print (f'Нужно перевернуть {tails_count} монет')
else :
    print (f'Нужно перевернуть {eagle_count} монет')