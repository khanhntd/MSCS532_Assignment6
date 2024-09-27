import helper

class Matrices:
  def __init__(self) -> None:
    self.matrices = []

  # insertRow will insert an array of integer values to
  # matrics at the target row
  # Time Complexity: O(1) (O(n) when shifting the elements to new array)
  # https://stackoverflow.com/a/7770654
  def insertRow(self, row: int, values: list[int]) -> None:
    self.matrices.insert(row, values)

  # insertColumn will insert all the values into target column
  # Time Complexity: O(n * m)
  def insertColumn(self, column:int, values: list[int]) -> None:
    for index in range(len(self.matrices)):
        self.matrices[index].insert(column, values[index])

  # Remove the row of matrics
  # Time complexity: O(n) (when reducing the size and shift the elements to new array)
  def removeRow(self, row: int):
    del self.matrices[row]

  # Remove the column of matrics
  # Time complexity: O(n * m) (when reducing the size and shift the elements to new array)
  def removeCol(self, column: int):
    for row in self.matrices:
        del row[column]

  # Access will access an element in the matrices
  # Time Complexity: O(1)
  def access(self, row: int, column: int) -> int:
    if row < 0 or row > len(self.matrices) - 1 or column < 0 or column > len(self.matrices[row]) -1:
      print("Invalid index at row ", row, " and ", column)
      return -1

    return self.matrices[row][column]

  def print(self):
    for index in range(len(self.matrices)):
      print(self.matrices[index], end=" ")
    print("\n")

def runBasicOperation():
  matrices = Matrices()
  numberOfElements = 3
  for row in range(numberOfElements):
      randomArray = helper.generateRandomArray(numberOfElements = numberOfElements)
      matrices.insertRow(row, randomArray)

  print("The values of matrices before inserting column")
  matrices.print()
  randomArray = helper.generateRandomArray(numberOfElements = numberOfElements)
  print("The values for inserting column are", randomArray)
  matrices.insertColumn(2, randomArray)
  print("The values of matrices after inserting element at column 2")
  matrices.print()
  matrices.removeRow(2)
  print("The values of matrices after removing row 2")
  matrices.print()
  matrices.removeCol(2)
  print("The values of matrices after removing column 2")
  matrices.print()
  print("The values of matrices at row 1 and index 1 is: ", matrices.access(1, 1))
  matrices.print()