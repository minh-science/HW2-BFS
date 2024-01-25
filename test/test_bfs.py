# write tests for bfs
import pytest
from search import graph
import networkx as nx

# filename= "data/citation_network.adjlist"
tiny_network = nx.read_adjlist("data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";") 
citation_network = nx.read_adjlist("data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    my_bfs = graph.Graph(filename= "data/tiny_network.adjlist").bfs(start= "Martin Kampmann")
    my_bfs.remove('Martin Kampmann') # written BFS algorithm contains the start node 
    nx_bfs = [x[1] for x in nx.bfs_edges(tiny_network, source = "Martin Kampmann") ]
    assert my_bfs == nx_bfs

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
    my_bfs = graph.Graph(filename= "data/citation_network.adjlist").bfs(start= "Martin Kampmann")
    nx_bfs = [x[1] for x in nx.bfs_edges(citation_network, source = "Martin Kampmann") ]
    my_bfs.remove('Martin Kampmann') # written BFS algorithm contains the start node 
    assert my_bfs == nx_bfs

    #shortest paths 
    my_bfs_path = graph.Graph(filename= "data/citation_network.adjlist").bfs(start= "Martin Kampmann", end = "Michael Keiser")
    nx_bfs_paths = [i for i in nx.all_shortest_paths(G=citation_network, source="Martin Kampmann", target= "Michael Keiser") ]
    # for i in nx_bfs_paths:
    #     print(i)
    assert my_bfs_path in nx_bfs_paths
    
    

test_bfs()