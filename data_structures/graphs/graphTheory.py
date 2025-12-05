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




