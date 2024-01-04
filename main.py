import math
import datetime
Greeting = ('', 'У этого калькулятора есть несколько режимов работы:', 'Обычный калькулятор — 1', 'Конвертация длины — 2',
            'Конвертация масс — 3', 'Калькулятор вкладов — 4', 'Перевод из различных систем счисления в десятичную — 5',
            'Интервал времени — 6', 'Чтобы остановить программу введите "стоп" (без кавычек)')
GreetingMath = ('Арабские цифры', 'Сложение — "+"', 'Вычитаение — "-"', 'Умножение — "*"', 'Деление — "/"',
                '\nВозведение в степень — "^"', 'Факториал — "!"', 'Квадратный корень — "√(" (ALT + Num251)',
                '\nЧисло π — "Pi"', 'Математическую константу — "E"', 'А также: sin, cos, tan, ln, lg')
MathConvertions = {'√': 'isqrt', 'ln': 'log(2.71828182846, ', 'lg': 'log10( ', 'Pi': 'pi ', 'E': 'e '}
OtherMathAct = ("sin", "cos", "tan")

GreetingLength = ('Поддерживаемые единицы измерения:', 'Километр — км', 'Метр — м', 'Дециметр — дм', 'Сантиметр — см',
                  '\nМиллиметр — мм', 'Микрометр — мкм', 'Нанометр — нм', "Пример: 2 см дм")
LenghtGraph = {'нм': 0, "мкм": 1, "мм": 2, "см": 3, "дм": 4, "м": 5, "км": 6}
LenghtGraphConvertations = {0: 1000, 1: 1000, 2: 10, 3: 10, 4: 10, 5: 10, 6: 1000}

GreetingMass = ('Поддерживаемые единицы измерения:', "Миллиграмм - мг", "Микрограмм — мкг", 'Грамм — г',
                'Килограмм — кг', "Тонна - т", "Центнер - ц", "Карат - кр", "Пример: 2 г кг")
MassGraph = {'мкг': 0, "мг": 1, "г": 2, "кг": 3, "т": 4, "ц": 5, "кр": 6} # ДОДЕЛАТЬ
MassGraphConvertations = {0: 1000, 1: 1000, 2: 1000, 3: 1000, 4: 1000, 5: 10, 6: 500000}

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
    for _ in range(expression.count('!')):
        pastStr = expression[:expression.index('!')]
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

    try:
        result = f"Результат: {eval(expression)}"
    except SyntaxError or NameError:
        result = 'Ошибка! Вы либо ввели неподдерживаемый символ, либо не закрыли скобку.'

    return result

def MathLength(number: str, mode: int): # mode 1 - длина, 2 - масса

    number, Place1, magnitude2 = float(number.split()[0]), number.split()[1], number.split()[2]

    try:
        if mode == 1:
            Place1 = LenghtGraph[Place1]
            Place2 = LenghtGraph[magnitude2]
        else: # mode == 2
            Place1 = MassGraph[Place1]
            Place2 = MassGraph[magnitude2]
    except KeyError:
        return "Ошибка! Введено неправильно!"

    if Place1 < Place2:
        while Place1 != Place2:
            Place1 += 1
            number = number / LenghtGraphConvertations[Place1] if mode == 1 else number / MassGraphConvertations[Place1]
    elif Place1 > Place2:
        while Place1 != Place2:
            Place1 -= 1
            number = number * LenghtGraphConvertations[Place1] if mode == 1 else number * MassGraphConvertations[Place1]

    return f'Результат: {number} {magnitude2}'

def Profit(Summa: float, Deadline: int, Begin: str, Bet: int, Capitalization: bool):
    InitialSumma = Summa
    day, month, year = int(Begin.split('/')[0]), int(Begin.split('/')[1]), int(Begin.split('/')[2])
    schedule = ['Дата        Начислено процентов    Изменение баланса	Выплата	    Баланс', # Таблица
               f"{Begin}  0 ₽{' ' * 19} + {Summa} ₽ {' ' * (15 - len(str(Summa)))} 0 ₽ {' ' * 7} {Summa} ₽"]
    Accrued = 0 # Всего начислено
    i = 0
    while i != Deadline:
        i += 1
        month += 1
        if month == 13:
            year += 1
            month = 1
        Adding = round(Summa / 100 * Bet / 12, 2) # начисляемый процент за 1 месяц
        if Capitalization:
            BalanceСhange = Adding 
            Summa += BalanceСhange
            Payout = 0
        else:
            BalanceСhange = 0
            Payout = Adding
        Accrued += Adding
        schedule.append(f'{day if day >= 10 else "0"+str(day)}/{month if month >= 10 else "0"+str(month)}/{year}  {Adding} ₽ {" " * (19 - len(str(Adding)))} + {BalanceСhange} ₽{" " * (16 - len(str(BalanceСhange)))} {Payout} ₽ {" " * (8 - len(str(Payout)))} {Summa} ₽') # страшно выглядящае заполнение таблицы
    schedule.append(f'Итого:      {Accrued} ₽ {" " * (52 - len(str(Accrued)))} {Summa} ₽')

    Increase = f"Прирост капиталла {int((Summa - InitialSumma) / InitialSumma * 100)} %"
    return schedule, Increase

def Hello():
    while True:
        print(*Greeting, sep='\n')
        mode = input('Выберите режим: ')
        if mode == '1':
            print('Калькулятор поддерживает:', *GreetingMath, '\nПример: 2.1+8^2-cos(6+Pi)*(80!-√(250))')
            print(Math(input("\nВведите выражение:\n")))
        elif mode == '2':
            print(*GreetingLength, sep=', ')
            print(MathLength(input("\nВедите число, единицу измерения вашего числа и во что перевести:\n"), 1))
        elif mode == '3':
            print(*GreetingMass, sep=', ')
            print(MathLength(input("\nВедите число, единицу измерения вашего числа и во что перевести:\n"), 2))
        elif mode == '4':
            Summa = float(input("Сумма вклада (₽): "))
            DeadLine = int(input("Срок размещения (мес.): "))
            Begin = input("Начало срока (сегодня / день/месяц/год): ")
            Begin = datetime.datetime.today().strftime("%d/%m/%Y") if Begin == 'сегодня' else Begin
            Bet = int(input("Процентная ставка (%): "))
            print('Капитализация — свойство вклада, при котором начисленные проценты не отдаются на руки держателю,',
                  '\nа прибавляются к вкладу. Таким образом сумма вклада растет с каждой выплатой процентов.')
            Capitalization = True if input("Капитализация процентов (да/нет): ") == 'да' else False
            table, Increase = Profit(Summa, DeadLine, Begin, Bet, Capitalization)
            print('', *table, Increase, '', sep='\n')
        elif mode == '5':
            number, system = input("Число: "), int(input("Система счисления числа: "))
            print('Число в десятичной системе счисления', int(number, system))
        elif mode == '6':
            first_time = [int(el) for el in input('Введите первное время (формат: год/месяц/день/час/минута/секунда): ').split('/')]
            second_time = [int(el) for el in input('Введите второе время (формат: год/месяц/день/час/минута/секунда): ').split('/')]
            print(abs(datetime.datetime(*first_time) - datetime.datetime(*second_time)))
        else:
            break
    
if __name__ == '__main__':
    Hello()
