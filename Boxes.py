#  File: Boxes.py

#  Description:

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

def subsets(a, b, lo, size_nested_boxes, d):
  hi = len(a)
  if (lo == hi):
    if b != []:
      if (len(b) == size_nested_boxes):
        if (does_fit(b[0],b[1]) and does_fit(b[1],b[2]) and does_fit(b[2],b[3])):
          for i in range(len(b)):
              print(b[i])
          print()
        return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1,size_nested_boxes, d)
    subsets (a, b, lo + 1,size_nested_boxes, d)

def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []
  box_list2 = []

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

  # create a list that will hold the nested boxes
  nested_boxes = []

  # create a variable for the size of the nested boxes
  size_nested_boxes = 4
  
  # check the maximum length of the boxes
  max_length = 1
    for i in nested_boxes:
        if (len(i) > max_length):
            max_length = len(i)

  # get all subsets of boxes
  # for each subset check if they all fit and print
  # also making sure that only those larger than 2 are printed out
  if(max_length >= 2):
    print("Largest Subset of Nesting Boxes")
    subsets (box_list, nested_boxes, 0, size_nested_boxes, box_list2)
    
  else:
    print("No Nesting Boxes")

main()
