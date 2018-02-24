#  File: Boxes.py

#  Description: Assignment 6 — Nesting Combinations of Boxes

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335 

#  Unique Number: 51340

#  Date Created: 2/22/2018

#  Date Last Modified: 2/24/2018

def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()
  print (box_list)

  # create a list that will hold the nested boxes
  nested_boxes[]

  # create a variable for the size of the nested boxes
  max_length = 1

    # Go through all sets of nesting boxes and find ones with maximum length
  for entry in nested_boxes:
    if len(entry) > max_length:
      max_length = len(entry)

  # get all subsets of boxes


  # for each subset check if they all fit

  # add to list
  print(nested_boxes)


main()
