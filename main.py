
#
# def calculate(a, operation, b):
#     result = None
#
#     if operation == '+':
#         result = a + b
#     elif operation == '-':
#         result = a - b
#     elif operation == '/':
#         result = a / b
#     elif operation == '*':
#         result = a * b
#     else:
#         print('Неизвестная операция')
#
#     return result
#
#
#
#
# print(calculate(1, "+", 3))

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

while True:
    print(msg_0)
    oper_list = ['+', '-', '*', '/']
    x, oper, y = input().split()

    if x.isalpha() or y.isalpha():
        print(msg_1)
    elif oper not in oper_list:
        print(msg_2)
    else:
        print(f"x =  {type(x)}, y = {type(y)}, oper = {type(oper)}")
        break
