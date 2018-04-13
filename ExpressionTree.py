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
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items) - 1]

  def size(self):
    return len(self.items)

class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):

  def __init__ (self):
    self.root = Node(None)

  def createTree (self, expr):
    stk = Stack()
    operators = ["*","/","+","-"]
    equation = []
    equation = expr.split()
    current = self.root

    for val in equation:
      if (val == "("):
        current.lchild = Node(None)
        stk.push(current)
        current = current.lchild
      elif (val in operators):
        current.data = val
        stk.push(current)
        current.rchild = Node(None)
        current = current.rchild
      elif (val.isdigit()):
        current.data = val
        current = stk.pop()
      elif ("." in val):
        current.data = val
        current = stk.pop()
      elif (val == ")"):
        if (stk.isEmpty() is False):
          current = stk.pop()

  # Evaluating the expression
  # For our current example we get: 55
  def evaluate (self, aNode):
    # Check digits
    if aNode.data.isdigit():
      return eval(aNode.data)
    # Check dots
    elif ('.' in aNode.data):
      return eval(aNode.data)
    elif (aNode.data == "*"):
      return (self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild))
    elif aNode.data == '/':
      return (self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild))
    elif aNode.data == '+':
      return (self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild))
    elif aNode.data == '-':
      return (self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild))

  # in order traversal - left, center, right
  def in_order (self, aNode, order):
    if (aNode != None):
      #Create left child
      self.in_order (aNode.lchild, order)
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      #Create right child
      self.in_order (aNode.rchild, order)
      
    return order

  #Not printing in functions
  def preOrder (self, aNode, order):
    if (aNode != None):
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      #Create left child
      self.preOrder (aNode.lchild, order)
      #Create right child
      self.preOrder (aNode.rchild, order)
      
    return order

  def postOrder (self, aNode, order):
    if (aNode != None):
      #Create left child
      self.postOrder (aNode.lchild, order)
      #Create right child
      self.postOrder (aNode.rchild, order)
      #print(aNode.data)
      #order is the array
      order.append(aNode.data)
      
    return order

def main():

  txt_file = open ("expression.txt", "r")
  txt_reading = txt_file.read()
  tree1 = Tree()
  tree1.createTree(txt_reading)
  #answer = tree.evaluate(tree.root)
  print(str(txt_reading),"=", end = " ")
  print(tree1.evaluate(tree1.root), "\n")
  
  #Assign values to the root and the nodes
  print("Prefix Expression:", end = " " )
  for i in (tree1.preOrder(tree1.root,[])):
    print(str(i), end = " ")
    
  print("\n")
  print("Postfix Expression:", end = " " )
  for i in (tree1.postOrder(tree1.root,[])):
    print(str(i), end = ' ')
  print()
  # print



main()
