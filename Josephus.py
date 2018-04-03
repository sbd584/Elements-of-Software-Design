
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
    #self.previous = previous

class CircularList (object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert ( self, item ):
    first_one = self.first
    current = self.first
    new_link = Link (item)

    if (first_one == None):
      first_one = new_link
      new_link.next = self.first
      current = new_link
    
    while (current.next != first_one):
      current = current.next

    current.next = new_link
    new_link.next = first_one
    new_link.previous = current

  # Find the link with the given key (value)
  def find ( self, key ):
    first_key = self.first
    current = self.first

    if (current == None):
      return None

    if (first_key.data == key):
      return first_key

    while (current.data != key):
     if (current.data == key):
       return current

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
      pre = pre.next

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

    self.delete(current.data)

    return current.next

  def delete_helper( self, start, n):
    first_one = self.first
    current = self.find(start)
    pre = self.first

    count = 1

    while (pre.next != first_one):
      pre = pre.next

    while (current.data != start):
      if (current.next == first_one):
        return None

      pre = current
      current = current.next
           
    while (count < (n)):
      current = current.next
      count += 1

    #if (current == first_one):
      #first_one = current.next

    return current.data
    
  # Return a string representation of a Circular List
  def __str__ ( self ):

    first_one = self.first.next.next
    current = self.first
    string = ""

    if (first_one == None):
      print("")

    else:
      string += str(current.data) + "  "
      current.next
      while (current != first_one):
        string += str(current.data) + "  "
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

  return soldiers, start, key

def main():

  # Test read_file
  # Working
  in_file = open("josephus.txt", "r")
  n, location, elim = read_file(in_file)
  
  # Create soldiers linked list
  soldiers = CircularList()

  # Establish the number of soldiers
  for key in range (1, n + 1):
    soldiers.insert(key)

  print(soldiers)

  new_location = location

  while (soldiers.first.next != soldiers.first):
    first_soldier = soldiers.delete_after(location, elim)
    last_soldier = soldiers.delete_helper(location, elim)
    last_location = last_soldier.data
    new_location = new_location.data
    print(last_location)

  print()
  print(soldiers)

  #while (soldiers.first.next != soldiers.f  irst):

  in_file.close()
  
main()
