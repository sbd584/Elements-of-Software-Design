#  File: TestLinkedList.py

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
  def __init__ (self,data,next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def get_num_links (self):
    current = self.first
    count = 0
    while(current != None):
      current = curent.next
      count += 1
    if(current == None):
      return count

  # add an item at the beginning of the list
  def insert_first (self, item):
    new_link = Link (item)
    new_link.next = self.first
    self.first = new_link

  # add an item at the end o  f a list
  def insert_last (self, item):
    new_link = Link (item)
    current = self.first
    if (current == None):
      self.first = new_link
      return
    while (current.next != None):
      current = current.next
    current.next = new_link

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item):
    new_link = Link(item)
    current = self.first
    if(current == None):
      self.first = new_link
      return
    while(current != None):
      if(current.next == None):
        current.next = new_link
        return
      if(current <= item and current.next > item):
        right_side = current.next
        current.next = new_link
        new_link.next = right_side
        return
      current = curent.next

  # search in an unordered list, return None if not found
  # Check each and every one
  def find_unordered (self, item):
    current = self.first
    while(current != None):
      if (current == item):
        return current
      current = current.next
    if (current == None):
      return None

  # Search in an ordered list, return None if not found
  def find_ordered (self, item):
    current = self.first
    while(current != None):
      if (current == item):
        return current
      if (current < item and current.next > item):
        return None
      current = current.next
    if (current == None):
      return None

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        previous = current
	current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):

  # Copy the contents of a list and return new list
  def copy_list (self):

  # Reverse the contents of a list and return new list
  def reverse_list (self):

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    while(current != None):
      if(current.next == None):
        current = current.next
        continue
      if(current.next < current):
        return False
      current = current.next
    if(current == None):
      return True

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    current = self.first
    if (current == None):
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    current1 = self.first
    current2 = other.first
    if(current1 != None and current2 != None):
      while(current1 != None):
        if(current2 == None):
          return False
        if(current1 != current2):
          return False
        current1 = current1.next
        current2 = current2.next
    elif((current1 == None and current2 == None):
      return True
    #Checks if current2 is longer than current1
    else:
      return False
  # Return a new list, keeping only the first occurence of an element and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):

  #def deleteLink (self, data):
    #current = self.first
    #previous = self.first

    #if (current == None):
      #return None

    #while (current.data != data):
      #if (current.next == None):
        #return None
      #else:
        #previous = current
	#current = current.next

    #if (current == self.first):
      #self.first = self.first.next
    #else:
      #previous.next = current.next

    #return current

def main():
  # Test methods insert_first() and __str__() by adding more than 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered()
  # Consider two cases - item is there, item is not there

  # Test method find_ordered()
  # Consider two cases - item is there, item is not there

  # Test method delete_link()
  # Consider two cases - item is there, item is not there

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()
