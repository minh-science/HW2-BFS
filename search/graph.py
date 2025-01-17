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
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";") 
    
    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        Q = [start] # initialize the queue
        visited = [start] # initialize the list of visited nodes  

        V = self.graph.nodes()

        if len(V) == 0:
            raise ValueError("has no nodes")

        X = [] # discovered list of nodes
        Y = [] # frontier list of nodes 
        d = {v:float('inf')  for v in V} # assign distances for all nodes other than the start node to be infinity
        d[start] = 0 
        prev = {v : None for v in V} # initialze dictionary to store the preceding node 
     
        while Q:
            v = Q.pop(0)
            
            # get neighbors of current node 
            try:
                N = list(self.graph.neighbors(v))
            except:
                raise ValueError(f"no edges connecting start: {start}")

            
            # append neighbors to frontier
            for w in N: 
                if w not in visited: 
                    visited.append(w)
                    Q.append(w)

                # update distance and previous nodes 
                if d[v] +1 < d[w]:
                    d[w] = d[v]+ 1
                    prev[w] = v

                # Update X and Y
                if w not in X and w not in Y:
                    Y.append(w)
                if w in Y:
                    Y.remove(w)
                    X.append(w)

            # find path from start to end
            if end is not None and v == end:
                shortest_path = self.construct_path(prev, start,end)
                return shortest_path

        if end != None:
            return None
        else:
            return visited
        
    def construct_path(self, prev, start, end):
        """reconstructs path from end node to start node

        Args:
            prev (dictionary): dictionary of previous nodes of all traversed nodes
            start (string): the start node specified 
            end (string): end node, previously specified

        Returns:
            dictionary: path from start node to end node
        """
        path = []
        current_node = end
        while current_node is not None: 
            path.insert(0, current_node)
            current_node = prev[current_node]
        return path
    
