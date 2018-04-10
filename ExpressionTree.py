#  File: ExpressionTree.py

#  Description:

#  Student's Name:

#  Student's UT EID:

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

#class Stack (object):

class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):

  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  #def createTree (self, expr):

  #def evaluate (self, aNode):

  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  #def postOrder (self, aNode):
    #if (aNode != None):

def main():

  txt_file = open ('expression.txt', 'r')
  txt_reading = txt_file.read()
  print("\n",txt_reading)




main()
