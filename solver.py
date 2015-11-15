#! /usr/bin/env python3

def add(total, n, solution):
  return total + n, "(" + solution + " + " + str(n) + ")"
  
def multiply(total, n, solution):
  return total * n, solution + " * " + str(n)
  
def subtract(total, n, solution):
  return total - n, "(" + solution + " - " + str(n) + ")"
  
def divide(total, n, solution):
  return total / n, solution + " / " + str(n)
  
def reverse_divide(total, n, solution):
  return n / total, str(n) + " / " + solution
  
def reverse_subtract(total, n, solution):
  return n - total, "(" + str(n) + " - " + solution + ")"
  
operations = [add, multiply, subtract, divide, reverse_divide, reverse_subtract]
target = 24

solutions = []

def operate(remainingNumbers, total, solution):

  # Some divisions will not return integers, but let's assume that's okay.
  
  if len(remainingNumbers) == 0:
    # We've used all the numbers
    if (total == target) and (solution not in solutions):
      solutions.append(solution)
    return
  
  else:
  # Some numbers still remain
    for n in remainingNumbers:
      reducedNumbers = remainingNumbers.copy()
      reducedNumbers.remove(n)
    
      for operation in operations:
        try:
          newTotal, newSolution = operation(total, n, solution)
        except ZeroDivisionError:
          pass # Nothing specific to do; just don't make the recursive call.
        else:
          operate(reducedNumbers, newTotal, newSolution)
        

def number_input(prompt):
  num = input(prompt)
  try:
    return int(num)
  except:
    return number_input("Not a valid number. Try again: ")
      
      
if __name__ == "__main__":

  numbers = []
  for n in range(4):
    numbers.append(number_input("Enter a puzzle number: "))
  
  # The rules of the game do not allow starting at 0 so I can not use
  # 0 x 2 x 5 + (3 x 8) = 24
  # ie. I cannot start with operate (numbers, 0)
  # Therefore, we must call the operate function with the total preset
  # to each of the original numbers
  for n in numbers:
    reducedNumbers = numbers.copy()
    reducedNumbers.remove(n)
    operate(reducedNumbers, n, str(n))
    
  if len(solutions) == 0:
    print("No solutions found.")
  else:
    for solution in solutions:
      print(solution)
