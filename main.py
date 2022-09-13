#Calculator 
from art import logo

#adding 
def add(n1, n2):
  return n1 + n2

#subtraction
def subtract(n1, n2):
  return n1 - n2

#Multiplication
def multiply(n1, n2):
  return n1 * n2

#Division 
def divide(n1, n2):
  return n1 / n2


calc_operation = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
  }
  
def calculator():
  print(logo)

  num1 = float(input("What the first number?: "))
  for symbol in calc_operation:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What the next number?: "))
    calc_function = calc_operation[operation_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 =  answer 
    else: 
      should_continue = False 
      calculator()

calculator()
