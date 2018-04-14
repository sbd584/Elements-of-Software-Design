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

  # Prints out all nodes at the given level
  #def print_level (self, level):

  # Returns the height of the tree
  #def get_height (self):

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  #def num_nodes (self):

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

  # return the node with minimum value
  def min_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current



  # return the node with maximum value
  def max_node (self):
    current = self.root

    return current


  # delete a node with a given key
  def delete (self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else:
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node is a node with only a right child
    #elif (delete_node.lchild == None):
      #if (delete_node == self.root):
        #self.root = delete_node.rchild
      #elif (is_left):
        #parent.lchild = delete_node.rchild
      #else:
        #parent.rchild = delete_node.rchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node

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

    #while (count <= level):

      #if (count == level):
        #s = 
      #s = str(current1
      #current1 = current1.

  # Returns the height of the tree
  #def get_height (self):

  #def height (self, aNode, count)

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

def main():
    # Create three trees - two are the same and the third is different
    a_tree = Tree()
    c_tree = Tree()
    vals = 10
    for i in range(vals - 1):
      a_tree.insert(random.randint(1,50))
      c_tree.insert(random.randint(1,50))

    b_tree = a_tree
    
    b_tree.insert(11)
    # Test your method is_similar()

    print(type(a_tree))
    print(a_tree)

    print()
    print("Tree A and B are similar: ", str(a_tree.is_similar(b_tree)))
    #print("Tree A and C are similar: ", a_tree.is_similar(c_tree))
    #print("Tree B and C are similar: ", b_tree.is_similar(c_tree))
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
    # Get the total numbe of nodes a binary search tree
    print("Tree A has ", a_tree.num_nodes(), " number of nodes")
    #print("Tree B has ", b_tree.num_nodes(), " number of nodes")
    #print("Tree C has ", c_tree.num_nodes(), " number of nodes")
    print()

main()
