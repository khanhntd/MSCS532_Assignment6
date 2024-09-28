import helper
import random

# partitionArray will partition the array based on the pivot which can be chosen from median of median
# https://medium.com/@amit.desai03/median-of-median-on-medium-5ed518f17307; however, for simplicity, we will choose
# the last element of the array. Afterwards, return the pivot index to divide and conquer
def partitionArray(array: list[int], low: int, high: int) -> int:
  pivot = array[high]

  swapStartingIndex = low - 1
  # Partition the array based on the pivot:
  # The left side will be smaller than the pivot
  # The right side will be larger than the pivot
  for currentIndex in range(low, high):
    if array[currentIndex] < pivot:
      swapStartingIndex +=1
      array[currentIndex], array[swapStartingIndex] = array[swapStartingIndex], array[currentIndex]

  # Swap the pivot element with the next element of the array's left side
  # to divide the array into two parts completely
  array[swapStartingIndex + 1], array[high] = array[high], array[swapStartingIndex + 1]
  return swapStartingIndex + 1


# randomizedQuickSelect will follow three steps:
# Step 1: Choose the pivot randomly
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3:
# * If the kth is smaller than left array number of elements, that mean the kth should be on the left sub array
# * If the kth is within the range of pivot, then the kth should be the pivot
# * If the k is larger than the range of pivot, then the kth should be the the right sub array
# Time complexity: O(n) (worst case is O(n^2)
# Space complexity: O(n)
def randomizedQuickSelect(array: list[int], kth: int) -> int:
  if len(array) == 1:
        return array[0]

  pivot = random.choice(array)
  leftArray = [element for element in array if element < pivot]
  rightArray = [element for element in array if element > pivot]
  pivotCount = array.count(pivot)

  if kth < len(leftArray):
    return randomizedQuickSelect(leftArray, kth)
  elif kth < len(leftArray) + pivotCount:
    return pivot

  return randomizedQuickSelect(rightArray, kth - len(leftArray) - pivotCount)

# medianOfMedians will follow three steps:
# Step 1: Choose the pivot randomly based on median of medians
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3:
# * If the kth is smaller than left array number of elements, that mean the kth should be on the left sub array
# * If the kth is within the range of pivot, then the kth should be the pivot
# * If the k is larger than the range of pivot, then the kth should be the the right sub array
# Time complexity: O(n)
# Space complexity: O(n)
def medianOfMedians(array: list[int], kth: int) -> int:
  if len(array) <= 5:
      return sorted(array)[kth]

  medians = []
  # Divide into 5 groups
  for currentIndex in range(0, len(array), 5):
      subarray = array[currentIndex:currentIndex + 5]
      medians.append(sorted(subarray)[len(subarray) // 2])

  # https://medium.com/@amit.desai03/median-of-median-on-medium-5ed518f17307
  pivot = medianOfMedians(medians, len(medians) // 2)
  leftArray = [element for element in array if element < pivot]
  rightArray = [element for element in array if element > pivot]
  pivotCount = array.count(pivot)


  if kth < len(leftArray):
    return randomizedQuickSelect(leftArray, kth)
  elif kth < len(leftArray) + pivotCount:
    return pivot

  return randomizedQuickSelect(rightArray, kth - len(leftArray) - pivotCount)

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

  print("The smallest 3 element with quickselect is", randomizedQuickSelect(array, 2))
  print("The smallest 6 element with quickselect is", randomizedQuickSelect(array, 5))

  print("The smallest 3 element with median of medians is", medianOfMedians(array, 2))
  print("The smallest 6 element with median of medians is", medianOfMedians(array, 5))

  print("Sorting array for easier visiblity for finding the kth smallest element")
  quickSort(array, 0, len(array) - 1)
  printArray(array)