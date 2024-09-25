import random

def generateRandomArray(numberOfElements: int) -> list[int]:
  return [random.randint(0, 200) for _ in range(0, numberOfElements)]