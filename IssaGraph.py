


class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # create a List
    printed = []

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    printed.append(self.Vertices [v].label)
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        printed.append(self.Vertices[u].label)
        theStack.push(u)
    # the stack is empty let us reset the falgs
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return printed

# Edit this
  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()

    # create a List
    printed = []

    # Select a starting vertex(v) & make it current and mark it visited.
    #
    (self.Vertices[v]).visited = True
    printed.append(self.Vertices [v].label)
    theQueue.enqueue(v)

    # vist other vertices according to breadth
    while (not theQueue.isEmpty()):
      # get an adjacent unvisited vertex
      u = theQueue.dequeue()
      u2 = self.getAdjUnvisitedVertex (u)

      while (u2 != -1):
        (self.Vertices[u2]).visited = True
        printed.append(self.Vertices[u2].label)
        theQueue.enqueue(u2)
        u2 = self.getAdjUnvisitedVertex(u)

    # the queue is empty let us reset
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

    return printed

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertex, toVertex):
    edgeWeight = self.adjMat[self.getIndex(fromVertex)][self.getIndex(toVertex)]
    if (edgeWeight == 0):
      return -1
    else:
      return edgeWeight

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbors = []
    index = self.getIndex(vertexLabel)
    
    for i in range (len(self.Vertices)):
      if not (self.adjMat[index][i] == 0):
        neighbors.append(self.Vertices[i].label)
        
    return neighbors

  # get a copy of the list of vertices
  def getVertices (self):
    verts = []
    for i in self.Vertices:
      verts.append(i)
    return verts

  # delete an edge from the adjacency matrix
  # UnDirected: 2 way: delete both edges
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    vert1 = self.getIndex(fromVertexLabel)
    vert2 = self.getIndex(toVertexLabel)
    self.adjMat[vert1][vert2] = 0
    self.adjMat[vert2][vert1] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  # getNeighbors has to work
  def deleteVertex (self, vertexLabel):
      
    for vertex in self.Vertices:
      if (vertex.label == vertexLabel):
  
        index = self.getIndex(vertexLabel)

        for i in range(len(self.adjMat)):
          del self.adjMat[i][index]
        
        del self.adjMat[index]

class Edge (object):
  def __init__ (self, towardsVertext, leavingVertex, weight = 1):
    self.u = leavingVertex
    self.v = towardsVertext
    self.weight = weight

  def __lt__(self,other):
    return self.weight < other.weight
  def __le__(self,other):
    return self.weight <= other.weight
  def __eq__(self,other):
    return self.weight == other.weight
  def __ne__(self,other):
    return self.weight != other.weight
  def __ge__(self,other):
    return self.weight >= other.weight
  def __gt__(self,other):
    return self.weight > other.weight

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)
  # close file
  inFile.close()

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  # do depth first search
  print ("\nDepth First Search from " + startVertex)
  city_list = cities.dfs (startIndex)
  for city in (city_list):
    print(city)
  print()

  # do breadth first search
  print ("\nBreadth First Search from " + startVertex)
  city_list = cities.bfs (startIndex)
  for city in (city_list):
    print(city)
  print()

  # setting up citie's vertices/labels
  example = cities.getVertices()
  SE = str(example[0])
  SF = str(example[1])
  LA = str(example[2])
  DE = str(example[3])
  KC = str(example[4])
  CH = str(example[5])
  BO = str(example[6])
  NY = str(example[7])
  AT = str(example[8])
  MI = str(example[9])
  DA = str(example[10])
  HO = str(example[11])
  
  print(SE + " to " + SF + " Edge Weight: " + str(cities.getEdgeWeight (SE, SF)))
  print()

  # Neighbors
  print("Testing getNeighbors function:")
  print()
  
  for i in range (numVertices):
    print (str(example[i].label) + " Neighbors: " + str(cities.getNeighbors(str(example[i]))))
  print ()


  # Delete Edge

  print("Testing deleteEdge function:")
  print()
  print("Delete: " + SE + "- " + SF)
  print("Before:")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()
  
  cities.deleteEdge(SE,SF)
  
  print("After: ")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()

  # Delete Vertex

  print("Testing deleteVertex function:")
  print()
  print("Delete: " + SE + ", " + SF)
  print("Before:")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()
  
  cities.deleteVertex(SE)
  cities.deleteVertex(SF)
  
  print("After: ")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat)):
      print(cities.adjMat[i][j], end = " ")
    print()
  print()

main()
