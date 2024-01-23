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

    # def f_neighbors(self, start):
        # print( [i for i in self.graph.nodes()] )
        # print(type(self.graph))
        # n_iter = self.graph.successors(start)
        # print( next(n_iter)) 
        # for i in self.graph.nodes(): 
            # print(i)
            # if i == start:
                # print("look here", self.graph.nodes(i))
                # n_dict = next( self.graph.adjacency() )
        # for i, n_dict in self.graph.adjacency():
        #     # print(i)
        #     if i == start:
        #     #     # print(self.graph.nodes())
        #         print(f"intermediate nodes of {i}:", n_dict)
        # print(self.graph.nodes())
        # return 
    
    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        Q = []
        visited = []
        Q.append(start)
        visited.append(start)
        N = []
        # print("self.graph:", self.graph.nodes())

        # maybe try using successors? is a generator though
        # print(f"successors of start (node: {start}):", [i for i in self.graph.successors(start)] )
        while len(Q) > 0:
            # print("len Q:", len(Q) ) 
            v = Q.pop()
            # print("this is v", v) 
            N = []
            ed = self.graph.edges(nbunch = v) #neighbits
            print(f"edges of v: {v}:", ed)
            N = [i[1] for i in ed] 
            # i = next(self.graph.successors(v))

            # print(type(i), i )
            # print(type(N), N)
            # N_tuple = ()
            # if i not in N_tuple: 
            #     N_tuple + (next(self.graph.successors(v) ))
            # if i not in N:
            #     N.append(next(self.graph.successors(v) ) )
            #     print(i, N)
            
            # print("neighbors of of start", N)
            # print(self.graph)
            # # print("this is W", w)
            for w in N: 
                if w not in visited: 
                    visited.append(w)
                    Q.append(w)
        print("visited nodes", visited)
        return

# Graph(filename ="../data/tiny_network.adjlist").bfs(start = "Martin Kampmann")

print( Graph(filename= "../data/tiny_network.adjlist").bfs(start= "Martin Kampmann") )

# print( Graph(filename= "../data/citation_network.adjlist").bfs(start= "Martin Kampmann") )

# L = ["a", 'b', 'c']
# print(L)
# for i in range(0, len(L)):
#     print(L.pop())
# print(L)


# try doing diksthras or whateber