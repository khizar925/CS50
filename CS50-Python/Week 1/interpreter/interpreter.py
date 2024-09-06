expression = input ("Expression: ")

new_expression = expression.split()

x = float(new_expression[0])
y = float(new_expression[2])

match new_expression[1]:
    case '+':
        print (x + y)
    case '-':
        print (x - y)
    case '*':
        print (x * y)
    case '/':
        print (x / y)
