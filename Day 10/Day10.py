# Add
from art import logo

def add(n1, n2):
  return n1 + n2

# Subtract 
def subtract(n1, n2):
  return n1 - n2

# Multiply 
def muliply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2


operators = {
  "+": add, 
  "-": subtract, 
  "*": muliply, 
  "/": divide
}


def calculator():

  print(logo)

  num1 = float(input("What's the first number?: "))
  for operator in operators:
    print(operator)

  continue_calculation = True

  while continue_calculation:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    calculation_function = operators[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to to start a new calculation: ").lower() == "y":
      num1 = answer
    else:
      continue_calculation = False
      calculator()

calculator()
