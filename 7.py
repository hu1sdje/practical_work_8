text = input('Введите число:')
while not text.isdigit():
    print('Ошибка. Попробуйте ещё раз.')
    text = input('Введите число:')
else:
    print(f'Введено целое число: {text}')