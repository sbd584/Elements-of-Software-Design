#  File: Triangle.py

#  Description: Using exhaustive, divide and conquer, greedy, and dynamic programming searches

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:  51335

#  Unique Number: 51340

#  Date Created: March 4th, 2018

#  Date Last Modified: March 9th, 2018

import time

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):

  for i in range(2 ** (len(grid) - 1)):
    b = grid[0][0]
    j = 0
    
    if (i == len(grid)):
      b.append(c)
  else:
    c += grid[j][i]
    if (i == 0):
      return exhaustive_search(grid, i + 1, j + 1, b, c)
    
    return exhaustive_search(grid, i, j + 1, b, c)

# returns the greatest path sum using greedy approach
def greedy (grid):

  index = 0
  j = 0

  for i in range(len(grid) - 1):
    j += grid[i][index]
    
    if (grid[i + 1][index] > grid[i + 1][index + 1]):
      index = index
    else:
      index += 1
        
  j += grid[i + 1][index]
  
  return grid[i + 1][j]

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid, i, j):

  if (i >= len(grid)):
    return 0
  
  else:
    grid1 = rec_search(grid, i + 1, j)
    grid2 = rec_search(grid, i + 1, j + 1)
    i = max(grid1, grid2) + int(grid[i][j])
    
  return i

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):

  for i in range(len(grid) - 2, -1, -1):
    for j in range(i + 1):
      grid.append(grid[i][j] + max(grid[i + 1][j]), grid[i + 1][j + 1])

  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle CHECK THIS LCODE
def read_file (file):
      
  grid = []

  num_lines = file.readline()
  num_lines = num_lines.strip()
  num_lines = int(num_lines)
  
  for line in range(num_lines):
    line = file.readline()
    line = line.split()
    for i in line:
      line = int(i)
      grid.append(line)
      
  return grid

def main ():
  grid = []
  # read triangular grid from file
  in_file = open("triangle.txt", "r")
  grid = read_file(in_file)

  ti = time.time()
  # output greatest path from exhaustive search
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search

  #The greatest path sum through exhaustive search is 23.
  #The time taken for exhaustive search is x seconds.

  ti = time.time()
  # output greates path from greedy approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach

  #The greatest path sum through greedy search is 23.
  #The time taken for greedy approach is x seconds.

  ti = time.time()
  # output greates path from divide-and-conquer approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach
  
  ##r_max = rec_search(grid, 0, 0)
  ##r_max = max(r_max)
  ##print("The greatest path sum through dynamic programming is ", r_max, ".")
  ##print("The time taken for dynamic programming is", del_t, "seconds.")

  #The greatest path sum through recursive search is 23.
  #The time taken for recursive search is x seconds.

  ti = time.time()
  # output greates path from dynamic programming
  dynamic_prog(grid)
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming
  
  print("The greatest path sum through dynamic programming is ", int(dynamic_prog(grid)), ".")
  print("The time taken for dynamic programming is", del_t, "seconds.")

  #The greatest path sum through dynamic programming is 23.
  #The time taken for dynamic programming is x seconds.

if __name__ == "__main__":
  main()
