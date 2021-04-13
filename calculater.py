number_1 = int(input("Enter your the first number: "))
number_2 = int(input("Enter your the second number: "))

operation = input('''
Please type in the math operation you would like to complete:
+ sum
-  subtraction
* multiplication
/ division
** power
sin  sinus
fac factorial

''')

if operation == '+':
    output_number = number_1 + number_2
    print( "{} + {} = {}" .format(number_1, number_2, output_number))
elif operation == '-':
    output_number = number_1 - number_2
    print( "{} - {} = {}" .format(number_1, number_2, output_number))
elif operation == '*':
    output_number = number_1 * number_2
    print( "{} * {} = {}" .format(number_1, number_2, output_number))
elif operation == '/':
    output_number = number_1 / number_2
    print( "{} / {} = {}" .format(number_1, number_2, output_number))
elif operation == '**':
    output_number = number_1 ** number_2
    print( "{} ** {} = {}" .format(number_1, number_2, output_number))
elif operation == 'sin':
    output_number = number_1 {math.sin()} number_2
    print( "{} ** {} = {}" .format(number_1, number_2, output_number))
elif  operation ==  'fac':
    output_number = number_1 {math.fac()} number_2
     print( "{} fac {} = {}" .format(number_1, number_2, output_number))   
else:
    print('enter operation! try again.')