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

class Stack (object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self,item):
    self.item.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):

  def __init__ (self):
    self.root = None

  #def createTree (self, expr):

  #def evaluate (self, aNode):

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)

  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lchild)
      self.postOrder (aNode.rchild)
      print(aNode.data)

def main():

  txt_file = open ('expression.txt', 'r')
  txt_reading = txt_file.read()
  print("\n",txt_reading)

  #Assign values to the root and the nodes




main()
