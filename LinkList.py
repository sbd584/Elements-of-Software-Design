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
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

class LinkedList (object):

  def __init__(self):
    self.first = None
  # get number of links
  def get_num_links (self):

  # add an item at the beginning of the list
  def insert_first (self, item):
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  # add an item at the end of a list
  def insert_last (self, item):
    newLink = Link(data)
    current = self.first
    if(current == None):
      self.first
    while(current.next != None):
      current = curent.next
    current.next = newLink

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item):

  # search in an unordered list, return None if not found
  def find_unordered (self, item):

  # Search in an ordered list, return None if not found
  def find_ordered (self, item):

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):

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

  # Return True if a list is empty or False otherwise
  def is_empty (self):

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):

  # Return a new list, keeping only the first occurence of an element and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):

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
