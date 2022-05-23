def calculator(a, b, s):
    """
    Калькулятор
    ===============
    Функция выполняющая над
    вещественными числами одну из четырех арифметических операций (сложение, вычитание, умножение или деление)
    
    #Inputs:
        :a: Первое значение
        :type a: float
        :b: Второе значение
        :type b: float
        :s: Арифмтическая операция (+,-,*,/)
    #Return:
        Результат арифметической операции
    """

    # a = float(input('a = '))
    # b = float(input('b = '))
    # s = input('Введите сивол:+,-,*,/')
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        if b != 0:
            return a / b
        else:
            return 'На ноль делить нельзя'
    else:
        return 'Неверный знак'


if __name__ == '__main__':
    calculator(3, 2, '*')
