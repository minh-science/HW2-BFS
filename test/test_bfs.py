# write tests for bfs
import pytest
from search import graph
import networkx as nx

# filename= "data/citation_network.adjlist"
filename= "data/tiny_network.adjlist"
graph_1 = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    print("my bfs", graph.Graph(filename= "data/tiny_network.adjlist").bfs(start= "Martin Kampmann") )
    # print( [x for x in nx.bfs_tree(G = graph.Graph(filename= "data/citation_network.adjlist"), source = "Martin Kampmann") ])
    print("other bfs", [x[1] for x in nx.bfs_edges(graph_1, source = "Martin Kampmann") ] )

test_bfs_traversal()    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    pass
