print('4 задание')
str = input('Введите сторку: ')
list = str.split(' ')
word = input('Поиск: ')
result = ''
for i in range(len(list)):
    if word == list[i]:
        result = list[i]

if result != '':
    print('Результат: ', result)
else:
    print('Такого слова НЕТ')

#python task4.py