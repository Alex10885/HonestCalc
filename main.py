def calculate(a, operation, b):
    result = None

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        result = a / b
    elif operation == '*':
        result = a * b
    else:
        print('Неизвестная операция')

    return result


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
memory = float(0)


while True:
    print(msg_0)
    oper_list = ['+', '-', '*', '/']
    x, oper, y = input().split()
    answer = ""

    if (x.isalpha() or y.isalpha()) and (y != 'M' or x != 'M'):
        # print(msg_1)
        if x == 'M':
            x = memory
        if y == "M":
            y = memory
    if oper not in oper_list:
        print(msg_2)
    else:

        try:
            result = calculate(float(x), oper, float(y))
            print(result)
        except ZeroDivisionError:
            print(msg_3)
            continue

        print(msg_4)
        answer = input().split()  # store result?
        if answer[0] == ("y" or "Y"):
            memory = result

        print(msg_5)
        answer = input().split()
        if answer[0] == ("n" or "N"):
            break
        if answer[0] == ("y" or "Y"):
            continue
