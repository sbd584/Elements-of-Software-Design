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
    previous = self.first
    current = self.first
    new_link = Link (item)

    if (current == None):
      self.first = new_link
      return

    while (current.next != first_one):
      previous = current
      current = current.next

    previous.next = new_link
    new_link.next = current.next

  # Find the link with the given key (value)
  def find ( self, key ):
    first_one = self.first
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != key):
      if (current.next == first_one):
        return None

      else:
        previous = current
        current = current.next

    if (current.data == key):
      return int(current)

    else:
      return None

  # Delete a link with a given key (value)
  def delete ( self, key ):
    first_one = self.first
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != key):
      if (current.next == first_one):
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
    first_one = self.first
    previous = self.first
    current = self.first
    count = 0
    location = start

  # Return a string representation of a Circular List
  # Wrong
  def __str__ ( self ):
    first_one = self.first
    current = self.first
    string = ""

    for i in range(self.get_num_links()):
      if (current != first_one):
        string += str(current.data) + "  "

        if (i > 8 and i % 9 == 0):
          print()

      if (current == first_one):
        print("")

      current = current.next

    return string

  def get_num_links (self):
    first_one = self.first
    current = self.first
    count = 1

    if (current == None):
      return 0

    while (current.next != first_one):
      current = current.next
      count += 1

    if (current.next == first_one):
      return count

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
  linked1.insert(0)
  print("insert 0")
  print(linked1)
  linked1.insert(1)
  print("insert 1")
  print(linked1)
  linked1.insert(2)
  print("insert 2 ")
  print(linked1)



main()
