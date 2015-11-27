#! /usr/bin/env python3

target = 24
threshold = .0000001
solutions = []

class chunk(object):
  def __init__(self, number, text = None):
    self.total = number
    if text is None:
      self.text = str(number)
    else:
      self.text = text


def add(a, b):
  newTotal = a.total + b.total
  newText = "(" + a.text + " + " + b.text + ")"
  return chunk(newTotal, newText)
  
def multiply(a, b):
  newTotal = a.total * b.total
  newText = "(" + a.text + " * " + b.text + ")"
  return chunk(newTotal, newText)

def subtract(a, b):
  newTotal = a.total - b.total
  newText = "(" + a.text + " - " + b.text + ")"
  return chunk(newTotal, newText)
  
def divide(a, b):
  newTotal = a.total / b.total
  newText = "(" + a.text + " / " + b.text + ")"
  return chunk(newTotal, newText)   
    
operations = [add, multiply, subtract, divide]



def operate(chunks):

  # Some divisions will not return integers, but let's assume that's okay.
  
  if len(chunks) == 1:
    # All compressed down to one chunk
    if (chunks[0].total - target < threshold) and \
       (target - chunks[0].total < threshold) and \
       (chunks[0] not in solutions):
       
      solutions.append(chunks[0])
    return
  
  else:
  # Some chunks still remain
    for chunk1 in chunks:
      chunksM1 = chunks.copy()
      chunksM1.remove(chunk1)
      for chunk2 in chunksM1:
        chunksM2 = chunksM1.copy()
        chunksM2.remove(chunk2)
        for operation in operations:
          try:
            newChunk = operation(chunk1, chunk2)
          except ZeroDivisionError:
            pass # Nothing specific to do; just don't make the recursive call.
          else:
            newChunks = chunksM2.copy()
            newChunks.append(newChunk)
            operate(newChunks)
        

def number_input(prompt):
  num = input(prompt)
  try:
    return int(num)
  except:
    return number_input("Not a valid number. Try again: ")
      
      
if __name__ == "__main__":

  numbers = []
  for n in range(4):
    numbers.append(chunk(number_input("Enter a puzzle number: ")))  
  operate(numbers)
    
  if len(solutions) == 0:
    print("No solutions found.")
  else:
    for solution in solutions:
      print(solution.text)
