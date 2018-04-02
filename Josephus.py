
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
  # Not too confident in this one yet
  def insert ( self, item ):
    first_one = self.first
    previous = self.first
    current = self.first

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

  # Return a string representation of a Circular List
  # Wrong
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
