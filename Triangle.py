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
  return

# returns the greatest path sum using greedy approach
def greedy (grid):
  return

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  return

def main ():
  # read triangular grid from file

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

  #The greatest path sum through recursive search is 23.
  #The time taken for recursive search is x seconds.

  ti = time.time()
  # output greates path from dynamic programming
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming

  #The greatest path sum through dynamic programming is 23.
  #The time taken for dynamic programming is x seconds.

if __name__ == "__main__":
  main()
