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

        X = []
        Y = []   
        V = self.graph.nodes()
        d = {v:float('inf')  for v in V} # assign d for all to be very high (should be infinity)
        d[start] = 0 
        prev = {v : None for v in V}
     

        while Q:
            v = Q.pop(0)

            # find path from start to end
            if end != None and v == end:
                shortest_path = self.construct_path(prev, start,end)
                return shortest_path
            
            # ed = self.graph.edges(nbunch = v) #neighbors
            N = list(self.graph.neighbors(v))
            # for i in N:
            #     if len(Y) == 0:
            #         Y.append(i)
            #         # print(Y)
            #     # for j in Y:
            #     #     print(j)
            #     #     if i != j:
            #     #         Y.append(i)
            # # print(N)
            # # i = next(self.graph.successors(v))

            
            # append to frontier
            for w in N: 
                if w not in visited: 
                    visited.append(w)
                    Q.append(w)

                if d[v] +1 < d[w]:
                    d[w] = d[v]+ 1
                    prev[w] = v

                # Update X and Y
                if w not in X and w not in Y:
                    Y.append(w)
                if w in Y:
                    Y.remove(w)
                    X.append(w)

        if end != None:
            return None
        else:
            return visited
        
    def construct_path(self, prev, start, end):
        path = []
        current_node = end
        while current_node is not None:
            path.insert(0, current_node)
            current_node = prev[current_node]
        return path
    
        

A = Graph(filename= "data/tiny_network.adjlist").bfs(start= "Martin Kampmann", end = "Michael Keiser") 
print(A)
# B = Graph(filename= "data/citation_network.adjlist").bfs(start= "Michael Keiser", end = "Martin Kampmann") 



Test1 = Graph(filename= "data/tiny_network.adjlist").bfs(start= "Martin Kampmann") 
# print(Test1)
