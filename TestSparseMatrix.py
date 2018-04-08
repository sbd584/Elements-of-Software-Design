
# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    s = ''
    s += "(" + str(self.col) + ", " + str(self.data) + ")" + "\n"
    
    return s

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # inserts a Link
  def insert_link (self, col, data):
    new_link = Link(col, data)
    current = self.first
    
    if (col == None):
      self.first = new_link
      return

    while (current.next != None):
      if (current.next == None):
        current.next = new_link
        return

      if (current.col <= col and current.next.col > col):
        right_side = current.next
        current.next = new_link
        new_link.next = right_side
        return

      else:
        current = current.next

  def delete_link (self, col, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None

      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next

    else:
      previous.next = current.next
        
  # return a String representation of a LinkedList
  def __str__ (self):
    current = self.first

    s = ''
    s += str(current.data)
    current = current.next
    
    while (current != None):
      s += ", " + str(current.data)
      current = current.next
      
    return s

class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.matrix = []
    self.row = row
    self.col = col

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    previous = self.matrix[row].first
    current = self.matrix[row].first

    while (current != None):
      if ((current.row == row) and (current.col == col)):
        if (data == 0):
          if (current.next == None):
            previous.next == None
          if (previous == current):
            self.matrix[row].first = current.next

          previous.next = current.next
          return

        current.data = data
        return

      if (current.col > col):
        if (data == 0):
          return

        new_link = Link (col, data)
        previous.next = new_link
        new_link.next = current
        return

    previous = current
    current = current.next         

  # add two sparse matrices
  def __add__ (self, other):
    if ((self.row != other.row) or (self.col != other.col)):
      return

    mat = Matrix(self.row, self.col)

    for i in range(self.row):
      for j in range(self.col):
        mat.matrix.insert_last(j, self.get_row(i)[j] + other.get_row(i)[j])

      #mat.matrix.append(row)

    return mat

  # multiply two sparse matrices
  def __mul__ (self, other):
    if (self.col != other.row):
      return

    mat = Matrix(self.row, other.col)
    for i in range(self.row):
      for j in range(other.col):
        s = 0
        for k in range(self.col):
          s += self.get_row(i)[k] * other.get_col(j)[k]
        mat.matrix.insert_last(j, s)
        
    return mat

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    row = self.col * [0]
    current = self.matrix[n]

    while (current != None):
      if (current.row == n):
          row[current.col] = current.data
      current = current.next

    return row
    

  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    col = self.row * [0]
    current = self.matrix[n]
      
    while (current != None) :
      if (current.col == n ):
        col[current.row] = current.data

      current = current.next
    
        #elif not (i > n):
          #current = current.next

        #else:
          #break
    
    return col

  # return a String representation of a matrix
  def __str__ (self):
    s = ''

    for i in range(self.row):
      row = self.get_row(i)
      s += str(row[0]).rjust(2)
      for j in range(self.col):
        s += str(row[j]).rjust(3) + " "

      s = s[0:-1]
      s += "\n"
        
    return s

def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  
  in_file.close()

main()
