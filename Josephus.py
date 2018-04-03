

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
    current = self.first
    new_link = Link (item)

    if (first_one == None):
      first_one = new_link
      new_link = current
      current = new_link
      return

    while (current.next != first_one):
      current = current.next

    current.next = new_link
    new_link.next = first_one

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

    if (first_one == None):
      return None

    while (current.data != key):
      if (current.next == first_one):
        return None

      pre = current
      current = current.next

    while (pre.next != first_one):
      pre = previous.next

    if (current == first_one):
      if (first_one == first_one.next):
        first_one = None

      else:
        first_one = current.next

    pre.next = current.next
    
    return current

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    first_one = self.first
    current = self.first
    count = 0
    location = start

    if (first_one == None):
      return None

    while (current.data != location):
      current = current.next

    count = 1

    while not (count == n):
      current = current.next
      count += 1

    #self.delete(current.data)

    return current.next

  # Return a string representation of a Circular List
  # Wrong
  def __str__ ( self ):

    first_one = self.first.next.next
    pre = self.first
    current = self.first
    string = ""

    if (first_one == None):
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

  for i in range (1, n + 1):
    soldiers.insert(i)

  

  while (soldiers.first.next != soldiers.first):
    

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
