import random

# generateRandomArray will only generate simple array
def generateRandomArray(numberOfElements: int) -> list[int]:
  return [random.randint(0, 200) for _ in range(0, numberOfElements)]

# generateArray will generate the corresponding array (e.g reverse sorted array)
def generateArray(numberOfElements: int, isSort: bool, sortIncreasing: bool) -> list[int]:
  array = [random.randint(0, 200) for _ in range(0, numberOfElements)]
  if (isSort):
    if sortIncreasing:
      array.sort()
    else:
      array.sort(reverse= True)

  return array

# printArray will print all the elements in the array
def printArray(array: list[int]):
    for i in range(len(array)):
        print(array[i], end=" ")
    print("\n")