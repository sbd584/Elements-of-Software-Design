#  File: Josephus.py

#  Description: Assignment 11 – Playing with LinkedLists

#  Student Name: Luis Carlos Orozco

#  Student UT EID: lco372

#  Partner Name: Samuel Beck Dillon

#  Partner UT EID: sbd584

#  Course Name: CS 313E

#  Unique Number:  51335 - sbd584

#  Unique Number: 51340 - lco372

#  Date Created: 4/01/2018

#  Date Last Modified: 4/02/2018

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class CircularList (object):
  # Constructor
  def __init__ ( self ):
    self.first = Link(None, None)
    #self.next = next
    self.first.next = self.first

  # Insert an element (value) in the list
  # Not too confident in this one yet
  def insert ( self, item ):
    first_one = self.first
    pre = self.first
    current = self.first
    new_link = Link (item)

    if (current == None):
      self.first = new_link
      return

    while (current.next != first_one):
      pre = current
      current = current.next

    pre.next = new_link
    new_link.next = current.next

  # Find the link with the given key (value)
  def find ( self, key ):
    first_one = self.first
    pre = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != key):
      if (current.next == first_one):
        return None

      else:
        pre = current
        current = current.next

    if (current.data == key):
      return int(current)

    else:
      return None

  # Delete a link with a given key (value)
  def delete ( self, key ):
    first_one = self.first
    pre = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != key):
      if (current.next == first_one):
        return None

      else:
        pre = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next

    else:
      pre.next = current.next

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    first_one = self.first
    pre = self.first
    current = self.first
    count = 0
    location = start

  # Return a string representation of a Circular List
  # Wrong
  def __str__ ( self ):

    first_one = self.first.next.next
    pre = self.first
    current = self.first
    string = ""

    if (current == None):
      print("")

    else:
      string += str(current.data) + "  "
      current.next
      while (current != first_one):
        string += str(current.data) + "  "
        pre = current
        current = current.next

    return string

def read_file (in_file):

  line = in_file.readline()
  line = line.strip()
  soldiers = int(line)

  line = in_file.readline()
  line = line.strip()
  start = int(line)

  line = in_file.readline()
  line = line.strip()
  key = int(line)

  return soldiers,start,key

def main():

  # Test read_file
  # Working
  in_file = open("josephus.txt", "r")
  reading = read_file(in_file)
  print(reading)

  linked1 = CircularList()
  #linked2 = CircularList()
  #linked3 = CircularList()

  #Test insert
  linked1.insert(1)
  print("insert 1")
  print(linked1)
  linked1.insert(3)
  print("insert 3")
  print(linked1)
  linked1.insert(2)
  print("insert 2 ")
  print(linked1)
  # Doesn't Work





main()
