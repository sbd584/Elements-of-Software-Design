#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import random

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):

  def __init__ (self):
    self.root = None

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    current1 = self.root
    current2 = pNode.root
    checker = False

    # Remove this
    print(current1.data)
    print(current2.data)

    # Exclusive statement in case no nodes exist whatsoever // Trees will be similar
    if ((current1 == None) and (currrent2 == None)):
      checker = True

    # While loop checking node is existent
    #while (current1 != None):
    # Traverse left children
    while ((current1.lchild != None) and (current2.lchild != None)):
      print(current1.data)
      print(current2.data)
      if ((current1.data) == (current2.data)):
        checker = True

      else:
        checker = False

      current1 = current1.lchild
      current2 = current2.lchild

    # Re-Initialize the Tree's node position
    current1 = self.root
    current2 = pNode.root

    # Traverse right children
    while ((current1.rchild != None) and (current2.rchild != None)):
      print(current1.data)
      print(current2.data)
      if ((current1.data) == (current2.data)):
        checker = True

      else:
        checker = False

      current1 = current1.rchild
      current2 = current2.rchild

    if (checker):
      return True

    else:
      return False

  # Prints out all nodes at the given level
  def print_level (self, level):
    current1 = self.root
    current2 = self.root
    count = 0

  # Returns the height of the tree
  #def get_height (self):


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    count = self.add_helper(self.root)

    return count

  def add_helper (self, aNode):
    if (aNode == None):
      return 0
    else:
      return self.add_helper(aNode.lchild) + 1 + self.add_helper(aNode.rchild)

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
      self.in_order(aNode.rchild)

def main():
    # Create three trees - two are the same and the third is different
    a_tree = Tree()
    c_tree = Tree()
    val1 = random.randint(0,20)
    val2 = random.randint(0,20)
    for i in range(val1):
      a_tree.insert(random.randint(1,50))

    for j in range(val2):
      c_tree.insert(random.randint(1,50))

    b_tree = a_tree
    # Test your method is_similar()

    print()
    print("Tree A and B are similar: ", a_tree.is_similar(b_tree))
    print("Tree A and C are similar: ", a_tree.is_similar(c_tree))
    print("Tree B and C are similar: ", b_tree.is_similar(c_tree))
    print()

    # Print the various levels of two of the trees that are different
    print("Tree A's levels: ")
    #for i in range(1,16):
        #a_tree.printLevel(i)
    print("Tree C's levels: ")
    #for i in range(1,16):
        #c_tree.printLevel(i)

    # Get the height of the two trees that are different
    #print("Tree A's height is: ", a_tree.get_height())
    #print("Tree C's height is: ", c_tree.get_height())
    print()
    # Get the total number of nodes a binary search tree
    print("Tree A has ", a_tree.num_nodes(), " number of nodes")
    print("Tree B has ", b_tree.num_nodes(), " number of nodes")
    print("Tree C has ", c_tree.num_nodes(), " number of nodes")
    print()

main()
