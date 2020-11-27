def my_div (*args):
    try:
        answer = numb_1 / numb_2
    except ZeroDivisionError:
        return 'Деление на ноль'
    return answer
numb_1 = int(input('Ввести число: '))
numb_2 = int(input('Ввести число: '))
print('Ответ:', my_div())



