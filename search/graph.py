import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";") # DIRECTED GRAPH!!! no actual direction
    
    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        Q = [start] # initialize the queue
        visited = [start] # initialize the list of visited nodes  
        # paths = [] 

        # maybe try using successors? is a generator though
        # print(f"successors of start (node: {start}):", [i for i in self.graph.successors(start)] )
        while len(Q) != 0:
            v = Q.pop(0)
            # ed = self.graph.edges(nbunch = v) #neighbors
            N = list(self.graph.neighbors(v))
            # print(N)
            # i = next(self.graph.successors(v))

            # find path from start to end
            # if end != None and v == end:
            #     print(visited)
            #     return "completed search", visited
            
            # append to frontier
            for w in N: 
                if w not in visited: 
                    # print(w)
                    visited.append(w)
                    Q.append(w)
                    print(visited)

        # print("visited nodes", visited)
        return visited


# A = Graph(filename= "data/citation_network.adjlist").bfs(start= "Martin Kampmann", end = "Michael Keiser") 
# B = Graph(filename= "data/citation_network.adjlist").bfs(start= "Michael Keiser", end = "Martin Kampmann") 


# filename= "data/tiny_network.adjlist"
# graph_1 = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
Test1 = Graph(filename= "data/tiny_network.adjlist").bfs(start= "Martin Kampmann") 

# print("other bfs", [x[1] for x in nx.bfs_edges(graph_1, source = "Martin Kampmann") ] )

# print("successors", [x  for x in nx.bfs_successors(graph_1, source = "Martin Kampmann") ] )
print("Test1:", Test1)




# try doing diksthras or whateber