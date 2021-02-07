print('1 задание')
str = input('Введите сторку: ')
list = str.split(' ')
max = list[0]

for i in range(len(list)):
    if len(list[i]) > len(max):
        max = list[i]

print('Самое длинное слово: ', max)
#python task1.py