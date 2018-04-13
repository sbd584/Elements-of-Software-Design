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
    self.stack = []

  def isEmpty(self):
    return (len(self.stack) == 0)

  def push(self,item):
    self.stack.append(item)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[len(self.stack)-1]

  def size(self):
    return len(self.stack)

class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):

  def __init__ (self):
    self.root = Node(None)

  def createTree (self, expr):
    cur = self.root
    stk = Stack()
    eqn = expr.split()

    for val in eqn:
      if (val == '('):
        stk.push(cur)
        cur.lchild = Node(None)
        cur = cur.lchild
      elif(val in ['*','/','+','-']):
        cur.data = val
        stk.push(cur)
        cur.rchild = Node(None)
        cur = cur.rchild
      elif(val.isdigit()):
        cur.data = val
        cur = stk.pop()
      elif('.' in val):
        cur.data = val
        cur = stk.pop()
      elif(val == ')'):
        if(stk.isEmpty() is False):
          cur = stk.pop()
        else:
          break

  # Evaluating the expression
  # For our current example we get: 55
  def evaluate (self, aNode):
    # Check digits
    if aNode.data.isdigit():
      return eval(aNode.data)
    # Check dots
    elif ('.' in aNode.data):
      return eval(aNode.data)
    elif aNode.data == '*':
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
      self.in_order (aNode.lchild,order)
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      #Create right child
      self.in_order (aNode.rchild,order)
    return order

  #Not printing in functions
  def preOrder (self, aNode, order):
    if (aNode != None):
      #print (aNode.data)
      #order is the array
      order.append(aNode.data)
      #Create left child
      self.preOrder (aNode.lchild,order)
      #Create right child
      self.preOrder (aNode.rchild,order)
    return order

  def postOrder (self, aNode, order):
    if (aNode != None):
      #Create left child
      self.postOrder (aNode.lchild,order)
      #Create right child
      self.postOrder (aNode.rchild,order)
      #print(aNode.data)
      #order is the array
      order.append(aNode.data)
    return order

def main():

  txt_file = open ('expression.txt', 'r')
  txt_reading = txt_file.read()
  tree1 = Tree()
  tree1.createTree(txt_reading)
  #answer = tree.evaluate(tree.root)
  print("\n",str(txt_reading),"=", end = " " )
  print(tree1.evaluate(tree1.root))

  print("Prefix Expression:", end = " " )
  for i in (tree1.preOrder(tree1.root,[])):
    print(str(i), end = ' ')

  print("\n","Postfix Expression:", end = " " )
  for i in (tree1.postOrder(tree1.root,[])):
    print(str(i), end = ' ')
  print()
  # print

main()
