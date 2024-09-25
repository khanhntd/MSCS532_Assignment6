import random

class Array:
  def __init__(self) -> None:
    self.array = []

  # Insert an element to the array
  # Time Complexity: O(n) (when shifting the elements to new array)
  # https://stackoverflow.com/a/7770654
  def insert(self, value: int) -> None:
    self.array.append(value)

  # Remove an element from an array using index
  # Time complexity: O(n) (when reducing the size and shift the elements to new array)
  def remove(self, index: int) -> None:
    if index < 0 or index > len(self.array) - 1:
      print("Invalid index ", index)
      return
    del self.array[index]

  # Access will access an element in the array
  # Time Complexity: O(1)
  def access(self, index: int) -> int:
    if index < 0 or index > len(self.array) - 1:
      print("Invalid index ", index)
      return

    return self.array[index]

  def print(self):
    for index in range(len(self.array)):
      print(self.array[index], end=" ")
    print("\n")

def generateRandomArray(numberOfElements: int) -> list[int]:
  return [random.randint(0, 200) for _ in range(0, numberOfElements)]

def runBasicOperation():
  array = Array()
  randomArray = generateRandomArray(numberOfElements = 20)
  for element in randomArray:
      array.insert(element)
  print("The values of array before removing")
  array.print()
  array.remove(2)
  print("The values of array after removing element at index 2")
  array.print()
  print("The element at index 4 is: ", array.access(4))

