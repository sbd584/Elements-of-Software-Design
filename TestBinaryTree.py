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

  ### is_similar using while loops ### // FOR TESTING PURPOSES
  ##### NOT ACTUALLY IMPLEMENTED TO RUN ON THE PROGRAM #######
  # Returns true if two binary trees are similar
  def is_similar_alt (self, pNode):
    current1 = self.root
    current2 = pNode.root
    checker = False

    # Exclusive statement in case no nodes exist whatsoever // Trees will be similar
    if ((current1 == None) and (currrent2 == None)):
      checker = True

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

  ### is_similar using while loops ends ###
  #### ORIGINAL FUNCTIONS BEGIN ###########

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    return self.identical (self.root, pNode.root)

  # Helper function for is_similar
  def identical (self, aNode, bNode):
    if (aNode == None) and (bNode == None):
      return True

    if (aNode != None) and (bNode != None):
      return ((aNode.data == bNode.data) and
              (self.identical (aNode.lchild, bNode.lchild)) and
              (self.identical (aNode.rchild, bNode.rchild)))

    return False

  # Prints out all nodes at the given level
  def print_level (self, level):
    list_array = []
    aNode = self.root
    level_check = 1
    if level == level_check:
      list_array.append(aNode.data)
      print(list_array)
      return
    self.get_level(level,1,aNode,list_array)
    if (len (list_array) == 0):
      return
    else:
      print(list_array)

  def get_level(self,level,current_level, aNode,list_array):
    if (aNode == None):
      return
    if (current_level > level):
      return
    else:
      if (current_level == level):
        list_array.append(aNode.data)
      else:
        self.get_level(level, current_level + 1, aNode.rchild,list_array)
        self.get_level(level, current_level + 1, aNode.lchild,list_array)

  # Returns the height of the tree
  def get_height (self):
    return self.height(self.root)

  def height (self, aNode):
    return 1 + max(self.height(aNode.lchild) if aNode.lchild != None else 0,
                   self.height(aNode.rchild) if aNode.rchild != None else 0)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    count = self.add_helper(self.root)
    return count

  # Helper function for num_nodes // Adds the number of nodes in a tree up
  def add_helper (self, aNode):
    if (aNode == None):
      return 0
    else:
      return self.add_helper(aNode.lchild) + 1 + self.add_helper(aNode.rchild)

def main():
    # Create three trees - two are the same and the third is different
    a_tree = Tree()
    c_tree = Tree()
    vals = 10
    for i in range(vals):
      a_tree.insert(random.randint(1,50))
      c_tree.insert(random.randint(1,50))

    b_tree = a_tree

    d_tree = Tree()
    e_tree = Tree()

    d_tree.insert(1)
    d_tree.insert(4)
    d_tree.insert(7)

    e_tree.insert(4)
    e_tree.insert(1)
    e_tree.insert(7)
    e_tree.insert(11)

    #b_tree.insert(11)
    # Test your method is_similar()

    print()
    print("Tree A and B are similar: ", str(a_tree.is_similar(b_tree)))
    print("Tree A and C are similar: ", str(a_tree.is_similar(c_tree)))
    print("Tree B and C are similar: ", str(b_tree.is_similar(c_tree)))
    print("Tree D and E are similar: ", str(d_tree.is_similar(e_tree)))
    print()

    # Print the various levels of two of the trees that are different
    print("Tree A's levels: ")
    for i in range(1,a_tree.get_height()+1):
      a_tree.print_level(i)
    print()
    print("Tree C's levels: ")
    for i in range(1,c_tree.get_height()+1):
      c_tree.print_level(i)
    print()
    print("Tree D's levels: ")
    for i in range(1,d_tree.get_height()+1):
      d_tree.print_level(i)
    print()
    print("Tree E's levels: ")
    for i in range(1,e_tree.get_height()+1):
      e_tree.print_level(i)
    print()

    # Get the height of the two trees that are different
    print("Tree B's height is: ", b_tree.get_height())
    print("Tree C's height is: ", c_tree.get_height())
    print("Tree D's height is: ", d_tree.get_height())
    print("Tree E's height is: ", e_tree.get_height())
    print()
    # Get the total numbe of nodes a binary search tree
    print("Tree A has " + str(a_tree.num_nodes()) + " number of nodes.")
    print("Tree C has " + str(c_tree.num_nodes()) + " number of nodes.")
    print("Tree E has " + str(e_tree.num_nodes()) + " number of nodes.")
    print()

main()
