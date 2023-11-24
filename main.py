import math
Greeting = ('У этого калькулятора есть несколько режимов работы:', 'Обычный калькулятор — 1', 'Конвертация длины — 2')
GreetingMath = ('Арабские цифры', 'Сложение — "+"', 'Вычитаение — "-"', 'Умножение — "*"', 'Деление — "/"',
                '\nВозведение в степень — "^"', 'Факториал — "!"', 'Квадратный корень — "√(" (ALT + Num251)',
                '\nЧисло π — "Pi"', 'Математическую константу — "E"', 'А также: sin, cos, tan, ln, lg')
MathConvertions = {'√': 'isqrt', 'ln': 'log(2.71828182846, ', 'lg': 'log10( ', 'Pi': 'pi ', 'E': 'e '}
OtherMathAct = ("sin", "cos", "tan")
GreetingLength = ('Поддерживаемые единицы измерения:', 'Километр — км', 'Метр — м', 'Дециметр — дм', 'Сантиметр — см',
                  '\nМиллиметр — мм', 'Микрометр — мкм', 'Нанометр — нм', "Пример: 2 см дм")
LenghtGraph = {'нм': 0, "мкм": 1, "мм": 2, "см": 3, "дм": 4, "м": 5, "км": 6}
LenghtGraphConvertations = {0: 1000, 1: 1000, 2: 10, 3: 10, 4: 10, 5: 10, 6: 1000}

def Math(expression: str):  # Математический калькулятор
    # замена клавиатурного возведения в степень в python
    expression = expression.replace('^', '**')
    # Словарь MathConvertions "вводимый символ операции": "операция модуля math"
    for key in MathConvertions:
        expression = expression.replace(key, f" math.{MathConvertions[key]}")

    # косинусы, синусы, тангенсы
    for value in OtherMathAct:
        if value in expression:
            expression = expression.replace(value, f" math.{value}")

    # факториал
    pastStr = expression[:expression.index('!')]
    for _ in range(expression.count('!')):
        print(pastStr, '----')
        temp = ''
        if pastStr[-1] == ')':  # Если факториал в скобках
            i = 0
            for el in pastStr[::-1]:
                temp += el
                if el == ')':
                    i += 1
                elif el == '(':
                    i -= 1
                if i == 0 and el != ' ':
                    temp = temp[::-1]
                    break
        else:
            for el in pastStr[::-1]:
                if el.isdigit():
                    temp += el
                else:
                    temp = temp[::-1]
                    break
        expression = expression.replace(f'{temp}!', f' math.factorial({temp}) ', 1)
        pastStr = expression[expression[::-1].index('lairotcaf'):]
        print(pastStr, '+++++++++')
    print(expression)
    try:
        result = f"Результат: {eval(expression)}"
    except SyntaxError or NameError:
        result = 'Ошибка! Вы либо ввели неподдерживаемый символ, либо не закрыли скобку.'

    return result

def MathLength(number1: str):

    number1, Place1, magnitude2 = float(number1.split()[0]), number1.split()[1], number1.split()[2]

    try:
        Place1 = LenghtGraph[Place1]
        Place2 = LenghtGraph[magnitude2]
    except KeyError:
        return "Ошибка! Введено неправильно!"

    if Place1 < Place2:
        while Place1 != Place2:
            Place1 += 1
            number1 = number1 / LenghtGraphConvertations[Place1]
            print(number1)
    elif Place1 > Place2:
        while Place1 != Place2:
            Place1 -= 1
            number1 = number1 * LenghtGraphConvertations[Place1]

    return f'Результат: {'{:.6g}'.format(number1)} {magnitude2}'

if __name__ == '__main__':
    for el in Greeting:
        print(el, sep='\n')
    mode = input('Выберите режим: ')
    if mode == '1':
        print('Калькулятор поддерживает:')
        for el in GreetingMath:
            print(el, end=', ')
        print('\nПример: 2.1+8^2-cos(6+Pi)*(80!-√(250))')
        print(Math(input("\nВведите выражение:\n")))
    elif mode == '2':
        for el in GreetingLength:
            print(el, end=', ')
        print(MathLength(input("\nВедите число, единицу измерения вашего числа и во что перевести:\n")))