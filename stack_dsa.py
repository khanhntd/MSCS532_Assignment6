import helper

class Stack:
  def __init__(self) -> None:
    self.stack = []

  # Insert an element to the stack as LIFO
  # Time Complexity: O(n) (when shifting the elements to new stack)
  # https://stackoverflow.com/a/7770654
  def insert(self, value: int) -> None:
    self.stack.append(value)

  # pop will remove the last element in the stack
  # Time complexity: O(n) (when reducing the size and shift the elements to new array)
  def pop(self) -> int:
    if len(self.stack) == 0:
      print("Empty stack")
      return -1

    lastElement = self.stack[len(self.stack) - 1]
    del self.stack[len(self.stack) - 1]
    return lastElement

  # Access will access an element in the stack
  # Time Complexity: O(1)
  def access(self, index: int) -> int:
    if index < 0 or index > len(self.stack) - 1:
      print("Invalid index ", index)
      return -1

    return self.stack[index]

  # top will get the top element of the stack
  # Time complexity: O(1)
  def top(self) -> int:
    if len(self.stack) == 0:
      print("Empty stack")
      return
    return self.stack[len(self.stack) - 1]


  def print(self):
    for index in range(len(self.stack)):
      print(self.stack[index], end=" ")
    print("\n")

def runBasicOperation():
  stack = Stack()
  randomArray = helper.generateRandomArray(numberOfElements = 20)
  print("Generate stack with random array", randomArray)
  for element in randomArray:
      stack.insert(element)
  print("The values of stack before poping element")
  stack.print()
  print("The poped element of an stack is ", stack.pop())
  print("The values of stack after poping element")
  stack.print()
  print("The element at index 4 is: ", stack.access(4))
  print("The top element of an stack is ", stack.top())