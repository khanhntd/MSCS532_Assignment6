import helper

class Queue:
  def __init__(self) -> None:
    self.array = []

  # enqueue will add an element to the queue as FIFO
  # Time Complexity: O(n) (when shifting the elements to new stack)
  # https://stackoverflow.com/a/7770654
  def enqueue(self, value: int) -> None:
    self.array.append(value)

  # dequeue will remove the first element in the array
  # Time complexity: O(n) (when reducing the size and shift the elements to new array)
  def dequeue(self) -> int:
    if len(self.array) == 0:
      print("Empty stack")
      return -1

    firstElement = self.array[0]
    del self.array[0]
    return firstElement

  # Access will access an element in the queue
  # Time Complexity: O(1)
  def access(self, index: int) -> int:
    if index < 0 or index > len(self.array) - 1:
      print("Invalid index ", index)
      return -1

    return self.array[index]

  # isEmpty will determine if the queue is empty or not
  def isEmpty(self) -> int:
    return len(self.array) == 0


  def print(self):
    for index in range(len(self.array)):
      print(self.array[index], end=" ")
    print("\n")

def runBasicOperation():
  queue = Queue()
  randomArray = helper.generateRandomArray(numberOfElements = 20)
  print("Generate queue with random array", randomArray)
  for element in randomArray:
      queue.enqueue(element)
  print("The values of queue before dequeue")
  queue.print()
  print("The top element of an array is ", queue.dequeue())
  print("The values of queue after dequeue")
  queue.print()
  print("The element at index 4 is: ", queue.access(4))
  print("Queue is empty: ", queue.isEmpty())