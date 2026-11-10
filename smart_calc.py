# 2. Smart Calculator
# - Addition, subtraction, multiplication and division.
# - Create separate functions.
# - Handle invalid inputs and division by zero.
# Concepts: functions, conditions, input
def add(a,b):
     return a+b
def sub(a,b):
     return a-b
def mul(a,b):
        return a*b
def div(a,b):
         return a/b
while True:
 try:
  print("!!!!!!WELCOME TO RAMU'S CALCULTIONS!!!!!!")
  a=int(input("Enter a number1:"))
  b=int(input('Enter a number2:'))
  option=int(input('Choose 1.Add 2.Subtract 3.Multiply 4.Divide:'))
  print('Choose the options (1,2,3,4):',option)
  if option==1:
    print('You choose addition(+)')
    print(add(a,b))
  elif option==2:
    print('You choose subtraction(-)')
    print(sub(a,b))
  elif option==3:
    print('You choose multiplication(*)')
    print(mul(a,b))
  elif option==4:
    print('You choose divition(/)')
    print(div(a,b))
  else:
    print("Invalid option!")
 except ZeroDivisionError:
  print('dont enter number with 0 enter other numbers')
 except ValueError:
  print('value error occured give integer value')
 choice = input("Do you want another calculation? (yes/no): ")
 if choice.lower()=='no':
    print("calculation stopped")
    break