#  File: Josephus.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified: 

class Link (object):
  def __init__ (self, data, next):
    self.data = data
    self.next = next

class CircularList (object):
  # Constructor
  def __init__ ( self ):
    self.first = Link(None, None)
    self.first.next = self.first

  # Insert an element (value) in the list
  def insert ( self, item ):
    self.first.next = Link(data, self.head.next)

  # Find the link with the given key (value)
  def find ( self, key ):
    current = self.first

    while (current != None):
      if  (current.data == item):
        return int(current)

      current = current.next

    if  (current == None):
      return None

  # Delete a link with a given key (value)
  def delete ( self, key ):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != key):
      if (current.next == None):
        return None

      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next

    else:
      previous.next = current.next

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):

  # Return a string representation of a Circular List
  def __str__ ( self ):

    string = ""

    current = self.first

    for i in range(self.get_num_links()):
      if (current != None):
        string += str(current.data) + "  "

        if (i > 8 and i % 9 == 0):
          print()

      if (current == None):
        print("")

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

def main():

main()
