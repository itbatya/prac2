print('3 задание')
str = input('Введите сторку: ')
list = str.split(' ')
min = list[0]

for i in range(len(list)):
    if len(list[i]) < len(min):
        min = list[i]

print('Самое короткое слово: ', min)
#python task3.py