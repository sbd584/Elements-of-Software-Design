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

  def createTree (self, expr):
    stack1 = Stack()

  # Evaluating the expression
  # For our current example we get: 55
  def evaluate (self, aNode):
    a = 55
    return a


  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      self.in_order (aNode.rchild)
    return order

  #Not printing in functions
  def preOrder (self, aNode):
    if (aNode != None):
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      #Create left child
      self.preOrder (aNode.lchild)
      #Create right child
      self.preOrder (aNode.rchild)
    return order

  def postOrder (self, aNode):
    if (aNode != None):
      #Create left child
      self.postOrder (aNode.lchild)
      #Create right child
      self.postOrder (aNode.rchild)
      #print(aNode.data)
      #order is the array
      order.append(aNode.data)
    return order

def main():

  txt_file = open ('./expression.txt', 'r')
  txt_reading = txt_file.read()
  tree = Tree()
  #tree.createTree(txt_reading)
  #answer = tree.evaluate(tree.root)
  #print("\n",txt_reading,"=",str(answer))

  #Assign values to the root and the nodes




main()
