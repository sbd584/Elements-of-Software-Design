
# Develop stack class with push and pop methods
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

# Node class
class Node (object):

  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

# Main Tree class
class Tree (object):

  def __init__ (self):
    self.root = Node(None)

  def createTree (self, expr):
    stk = Stack()
    operators = ["*", "/", "+", "-"]
    equation = []
    equation = expr.split()
    current = self.root

    # Go through the expression characters and append through the tree's children
    for val in equation:
      # Check for first parenthesis
      if (val == "("):
        current.lchild = Node(None)
        stk.push(current)
        current = current.lchild
      # Check for operators
      elif (val in operators):
        current.data = val
        stk.push(current)
        current.rchild = Node(None)
        current = current.rchild

      # Check for numbers
      elif (val.isdigit()):
        current.data = val
        current = stk.pop()

      # Check for dots
      elif ("." in val):
        current.data = val
        current = stk.pop()

      # Check for second parenthesis
      elif (val == ")"):
        if (stk.isEmpty() is False):
          current = stk.pop()

  # Evaluating the expression
  # For our current example we get: 55
  def evaluate (self, aNode):
    # Check for digits
    if aNode.data.isdigit():
      return eval(aNode.data)
    
    # Check for dots
    elif ("." in aNode.data):
      return eval(aNode.data)

    # Multiply if asterisk notation
    elif (aNode.data == "*"):
      return (self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild))

    # Divide if slash notation
    elif aNode.data == '/':
      return (self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild))

    # Add if sumation notation
    elif aNode.data == '+':
      return (self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild))

    # Subtract if subtraction notation
    elif aNode.data == '-':
      return (self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild))

  # in order traversal - left, center, right
  def in_order (self, aNode, order):
    if (aNode != None):
      # Create left child
      self.in_order (aNode.lchild, order)
      # print (aNode.data)
      # order is the array
      order.append(aNode.data)
      # Create right child
      self.in_order (aNode.rchild, order)
      
    return order

  # pre order traversal - center, left, right
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

  # post order traversal - left, right, center
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
  print(str(txt_reading) + " = "+ str(tree1.evaluate(tree1.root)) + "\n")
  
  #Assign values to the root and the nodes
  print("Prefix Expression:", end = " " )
  for i in (tree1.preOrder(tree1.root, [])):
    print(str(i), end = " ")
    
  print("\n")
  print("Postfix Expression:", end = " " )
  for i in (tree1.postOrder(tree1.root, [])):
    print(str(i), end = ' ')
  print()
  
main()
