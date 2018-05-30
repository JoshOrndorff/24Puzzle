#! /usr/bin/env python3

numbers = 4
target = 24
threshold = .0000001

class chunk(object):
  def __init__(self, number, text = None):
    self.total = number
    if text is None:
      self.text = str(number)
    else:
      self.text = text

  # For sorting
  def __lt__(self, other):
    return self.total < other.total

  def __eq__(self, other):
    return self.text == other.text

  def __hash__(self):
    return hash(self.text)

  def __str__(self):
    return self.text


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
       (target - chunks[0].total < threshold):

      print(chunks[0])

  else:
  # Some chunks still remain
    for chunk1 in chunks:
      chunksM1 = list(chunks) # Makes a copy
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
            newChunks.sort() # Should be O(n) because it was already sorted
            open.add(tuple(newChunks))


def number_input(prompt):
  num = input(prompt)
  try:
    return int(num)
  except:
    return number_input("Not a valid number. Try again: ")
      
      
if __name__ == "__main__":

  # Get the user input and initialize things
  operations = (add, multiply, subtract, divide)
  closed = set()
  open = set()
  initial = []
  for i in range(numbers):
    initial.append(chunk(number_input("Enter a puzzle number: ")))
  initial.sort()

  open.add(tuple(initial))

  # Execute the solution search
  while len(open) > 0:
    #TODO remove debugging line input("open: {} closed: {}".format(len(open), len(closed)))
    chunks = open.pop()
    if chunks not in closed:
      operate(chunks)
    closed.add(chunks)
