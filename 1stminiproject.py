class simplecalc:
    print('This is only a simple calculator! Enter two numbers pls!')
    num_1 = input('Enter no.1: ')
    num_2 = input('Enter no.2: ')
    operator = input('What operation do you want to do?: ')

    if operator == '+':
        calc_result = float(num_1) + float(num_2)
        print(calc_result)
    elif operator == '-':
        calc_result = float(num_1) - float(num_2)
        print(calc_result)
    elif operator == '/':
        calc_result = float(num_1) / float(num_2)
        print(calc_result)
    elif operator == '*':
        calc_result = float(num_1) * float(num_2)
        print(calc_result)
    else:
        print('Cant even enter a number loser')
        
