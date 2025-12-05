"""
The below is the basic notes for graphs in my Data structures and algorithms 
course. Graphs has 54 problems on takeUfoward and we will solve all of them under 
this directory. 

Lecture 1 : Types, Conventions and preliminaries. 

Difference between a directed graph and an undirected graph is that the directionality 
of an edge is specified in a directed graph and not in an undirected graph.

A graph is said to be cyclic if there exists a node such that there exists a path in the graph 
which starts from a particular vertex and ends at the same vertex. 

A graph is said to a directed cyclic graph if there exists a node such that there is a directed 
path from that node to itself. 

A directed graph which does not have a cycle in it is called a directed acyclic graph (DAG). 

Definition of a path:
Contains a lot of nodes and each of them are reachable. A particular node cannot appear twice in a path. 


Degrees in a graph: The number of edges from a particular vertex is called the degree of that vertex. The sum 
of degrees of all vertices in a graph is called the degree of the graph. Total degree of a graph = twice the number of edges. 
Every edge is associated to gtwo nodes and hence the above property. 

The indegree of a node in a directed graph is the number of incoming edges into a node. The outdegree of a vertex 
is the number of outgoing edges from a node. 

Some graphs which are called weighted graphs have edges with a number attached to them. The number on the edge denotes the 
weight on the particular edge.  

"""

def createAdjacenyMatrix(vertices, edges, edgeList): 
    adjMatrix = [[0 for _ in range(vertices + 1)] for _ in range(vertices + 1)]

    for i in range(0, edges): 
        node1, node2 = edgeList[i] 
        adjMatrix[node1][node2] = 1 
        adjMatrix[node2][node1] = 1 

    return adjMatrix
 
"""
Representing a graph in the form of an adjacency matrix is a little expensive as it takes a space complexity of 
O(n^2). The above is one way of representing a graph where the matrix indices denote the vertex and a value of 1
represents a 
"""

def createAdjacencyList(vertices, edges, edgeList):
    adjList = [[] for _ in range(vertices + 1)] 
    for i in range(0, edges): 
        node1, node2 = edgeList[i] 
        adjList[node1].append(node2)
        adjList[node2].append(node1) 

    return adjList 

"""
Adjacency list uses a space complexity of 2 * |e| because each edge is repeated twice in an 
undirected graph as all the edges are bidirectional in the same. 
"""


"""
How to store a weighted graph? 
"""

def createWeightedAdjacencyMatrix(vertices, edges, edgeList):
    adjMatrix = [[0 for _ in range(vertices + 1)] for _ in range(vertices + 1)]
    for i in range(0, edges): 
        nodes, weight = edgeList[i] 
        node1, node2 = nodes 
        adjMatrix[node1][node2] = weight 
        adjMatrix[node2][node1] = weight

    return adjMatrix
 

def main(): 
    numberOfVertices = 5 
    numberOfEdges = 6 
    edgeList = [((1,2), 9), ((1,3), 10), ((2,4), 8), ((3,4), 15), ((3,5), 19), ((4,5), 20)]

    adjacencyMatrix = createWeightedAdjacencyMatrix(numberOfVertices, numberOfEdges, edgeList) 
    print("ADJACENCY MATRIX: \n", adjacencyMatrix) 

    # adjacencyList = createAdjacencyList(numberOfVertices, numberOfEdges, edgeList) 
    # print("ADJACENCY LIST: \n", adjacencyList) 


main() 