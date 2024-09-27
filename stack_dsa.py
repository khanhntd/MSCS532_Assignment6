import helper

class Stack:
  def __init__(self) -> None:
    self.array = []

  # Insert an element to the stack as FILO
  # Time Complexity: O(n) (when shifting the elements to new stack)
  # https://stackoverflow.com/a/7770654
  def insert(self, value: int) -> None:
    self.array.append(value)

  # pop will remove the last element in the array
  # Time complexity: O(n) (when reducing the size and shift the elements to new array)
  def pop(self) -> int:
    if len(self.array) == 0:
      print("Empty stack")
      return -1

    lastElement = self.array[len(self.array) - 1]
    del self.array[len(self.array) - 1]
    return lastElement

  # Access will access an element in the stack
  # Time Complexity: O(1)
  def access(self, index: int) -> int:
    if index < 0 or index > len(self.array) - 1:
      print("Invalid index ", index)
      return -1

    return self.array[index]

  # top will get the top element of the stack
  def top(self) -> int:
    if len(self.array) == 0:
      print("Empty stack")
      return
    return self.array[len(self.array) - 1]


  def print(self):
    for index in range(len(self.array)):
      print(self.array[index], end=" ")
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