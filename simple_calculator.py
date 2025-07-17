# 🎉 Welcome to the Fun Calculator! 🎉
num1 = float(input('Enter first number '));
num2= float(input('Enter second number'));

print('choose the operation you want to perform:');

print('a:addition');
print('b: substraction');
print('c: multiplication');
print('d: division');

product = num1 * num2;
addition = num1 + num2;
substraction = num1 - num2;
division: num1/num2 if num2 != 0 else 'undefined';

if input('Enter Yout choice:') == 'a':
    print('The sum is:', addition);
elif input('Enter your Choice: ') == 'b':
    print('The difference is:', substraction);
elif input('Enter your choice: ') == 'c':
    print('The product is:', product);
elif input('Enter your choice:') == 'd':
        print('The quotient is:', division);
else:
    print('invalid choice, please try again.');


