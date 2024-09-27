import helper

class Node:
  def __init__(self, value) -> None:
    self.next = None
    self.value = value
class LinkedList:
  def __init__(self) -> None:
    self.head = None

  # insert will insert the element at the end of linkedlist
  # Time complexity: O(n)
  def insert(self, value:int) -> None:
    if self.head == None:
      self.head = Node(value = value)
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = Node(value = value)

  # remove will remove the element at an index
  # Time complexity: O(n)
  def remove(self, index: int) -> None:
    current = self.head
    previous = None
    if current is not None and index == 0:
      value = current.value
      self.head = current.next
      return value

    currentIndex = 0
    while current is not None and currentIndex != index:
      previous = current
      current = current.next
      currentIndex +=1

    if current is None:
      return -1

    value = current.value
    previous.next = current.next
    current = None
    return value

  # search will search and return the element at an index
  # Time complexity: O(n)
  def search(self, index:int) -> int:
    current = self.head
    currentIndex = 0
    while current.next is not None:
      if currentIndex == index:
        break
      current = current.next
      currentIndex +=1

    if current == None:
      return -1

    return current.value
  
  # print will print all element in the linked list
  # Time complexity: O(n)
  def print(self) -> None:
    current = self.head
    while current.next is not None:
      print(current.value, end=" ")
      current = current.next
    print("\n")

def runBasicOperation():
  linkedList = LinkedList()
  randomArray = helper.generateRandomArray(numberOfElements = 20)
  print("Generate linkedList with random array", randomArray)
  for element in randomArray:
      linkedList.insert(element)
  print("The values of linkedlist before poping element")
  linkedList.print()
  print("The removed element of an linked list at index 2 is ", linkedList.remove(2))
  print("The values of stack after removing an element")
  linkedList.print()
  print("The element at index 4 is: ", linkedList.search(4))