import helper
import random

def partitionArray(array: list[int], low: int, high: int, pivotIndex: int = -1) -> int:
  if pivotIndex < 0:
    pivotIndex = random.randint(low, high)

  array[pivotIndex], array[high] = array[high], array[pivotIndex]
  pivot = array[high]
  swapStartingIndex = low
  # Partition the array based on the pivot:
  # The left side will be smaller than the pivot
  # The right side will be larger than the pivot
  for currentIndex in range(low, high):
    if array[currentIndex] < pivot:
      array[currentIndex], array[swapStartingIndex] = array[swapStartingIndex], array[currentIndex]
      swapStartingIndex +=1

  # Swap the pivot element with the next element of the array's left side
  # to divide the array into two parts completely
  array[swapStartingIndex], array[high] = array[high], array[swapStartingIndex]
  return swapStartingIndex

# quickSelect will follow two steps:
# Step 1: Choose the pivot randomly
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3:
# * If the kth is smaller than pivot, that mean the kth should be on the left sub array
# * If the kth is larger than pivot, that mean the kth should be on the right sub array
# * If the kth is equal to pivot, that mean we have the kth smallest element
# Time complexity: O(nlog n) (worst case is O(n^2) for nearly sorted one)
# Space complexity: O(log n) (O(n) for nearly sorted one)
def quickSelect(array: list[int], low: int, high: int, kth: int) -> int:
  if low == high:
      return array[low]

  pivotIndex = partitionArray(array, low, high)
  if pivotIndex == kth:
    return array[pivotIndex]
  elif kth < pivotIndex:
    return quickSelect(array,low, pivotIndex - 1, kth)

  return quickSelect(array,pivotIndex + 1, high, kth)

# quickSelect will follow two steps:
# Step 1: Choose the pivot randomly based on median of medians
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3:
# * If the kth is smaller than pivot, that mean the kth should be on the left sub array
# * If the kth is larger than pivot, that mean the kth should be on the right sub array
# * If the kth is equal to pivot, that mean we have the kth smallest element
# Time complexity: O(nlog n) (worst case is O(n^2) for nearly sorted one)
# Space complexity: O(log n) (O(n) for nearly sorted one)
# Time complexity: O(nlog n) (worst case is O(n^2) for nearly sorted one)
# Space complexity: O(log n) (O(n) for nearly sorted one)
def medianOfMedians(array: list[int], low: int, high: int, kth: int) -> int:
  if low == high:
      return array[low]

  numberOfElements = high - low + 1
  medians = []

  # Divide into 5 groups
  for currentIndex in range(0, numberOfElements, 5):
      subarray = array[low + currentIndex:min(low + currentIndex + 5, high + 1)]
      medians.append(sorted(subarray)[len(subarray) // 2])

  mOfMedians = medianOfMedians(medians, 0, len(medians) - 1, len(medians) // 2)

  pivotIndex = partitionArray(array, low, high, array.index(mOfMedians))
  if pivotIndex == kth:
    return array[pivotIndex]
  elif kth < pivotIndex:
    return quickSelect(array,low, pivotIndex - 1, kth)

  return quickSelect(array,pivotIndex + 1, high, kth)

# printArray will print all the elements in the array
def printArray(array: list[int]):
    for i in range(len(array)):
        print(array[i], end=" ")
    print("\n")


# quickSort will following the three steps:
# Step 1: Choose the pivot (last element of the array)
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3: Repeat the same for the left side and right side
# Time complexity: O(n log n) (O(n^2) when the array is sorted either in descending or ascending)
# Space complexity: O(1)
# https://en.wikipedia.org/wiki/Quicksort
def quickSort(array: list[int], low: int, high: int):
  if low > high:
    return

  # Get the pivot index for the array
  pivot = partitionArray(array, low, high)
  # Perform the same implementation (choose pivot and divide) to the left side array
  quickSort(array, low, pivot - 1)
  # Perform the same implementation (choose pivot and divide) to the right side array
  quickSort(array, pivot + 1, high)

def runBasicOperation():
  array = helper.generateArray(numberOfElements=10, isSort=False,sortIncreasing=False)
  print("Before finding the kth smallest element")
  printArray(array)

  print("The smallest 3 element with quickselect is", quickSelect(array, 0, len(array) - 1, 2))
  print("The smallest 6 element with quickselect is", quickSelect(array, 0, len(array) - 1, 5))

  print("The smallest 3 element with median of medians is", medianOfMedians(array, 0, len(array) - 1, 2))
  print("The smallest 6 element with median of medians is", medianOfMedians(array, 0, len(array) - 1, 5))

  print("Sorting array for easier visiblity for finding the kth smallest element")
  quickSort(array, 0, len(array) - 1)
  printArray(array)