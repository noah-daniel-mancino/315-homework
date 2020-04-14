"""
Author: Noah Mancino
Description:
This script reads text representing a directed acyclic graph from standard
input. The text must begin with a line specifying the number of vertices, N,
followed by a line specifying the number of edges. Each subsequent line
consists of two positive integers seperated by a space, which represents an
edge from the first to the second. Aditionally, it is assumed that the edges
are listed in order of their tails (e.g the line "2 1" should never come
before the line "1 2"). Finally, it is assumed that each vertex is between 1
and N inclusive and that the topological ordering of the vertices matches the
counting ordering of the vertices.
"""
import sys
import math


class DirectedGraph:
    """
    A class for our directed graph. This class takes advantage of the 
    restrictions on input specified in the file doc string and is not meant for
    use outside this script.
    """

    def __init__(self, verticies):
        """
        Initializes an adjaceny list of a graph with no edges and the first n
        positive integers as verticies. This adjaceny list is stored in a
        dictionary.
        """
        self.largest = verticies # The largest vertex
        self.graph = {}
        for i in range(0, verticies):
            self.graph[i+1] = []

    @staticmethod
    def read_graph(): 
        """
        Reads a textual graph representation from standard input into a
        DirectedGraph object and returns that object.
        """
        raw_graph_text = sys.stdin.readlines()
        # First two lines contain number of verticies and number of edges
        # respectively. The number of edges is also the number of subsequent
        # lines in the text representation of the graph. 
        verticies, edges = int(raw_graph_text[0]), int(raw_graph_text[1])
        graph = DirectedGraph(verticies)
        # The next lines contain a pair of integers represented by spaces which
        # represent edges. The first int is the tail, the second is the head.
        for edge in range(2, edges + 2):
            tail, head = [int(num) for num in raw_graph_text[edge].split()]
            # Add the head to the tail's adjacency list
            graph.graph[tail].append(head)

        return graph

    def shortest_to_n(self):
        """
        Performs a breadth first search on the graph starting from vertex 1.
        Upon finding the largest vertex, the function will exit and return the
        length of the shortest path from 1 to the largest vertex in the graph. 
        If the search finishes before the largest vertex is found, return nan.
        """
        # This dict will be used both to keep track of which nodes have been
        # visited and the length of the path we are on. Initially, all
        # verticies are 'nan' away from 1.
        distances_dict = {n:float('nan') for n in range(1, self.largest + 1)}
        search_queue = []
        # We start off by visiting one and adding it to the queue.
        distances_dict[1] = 0
        search_queue.append(1)
        while search_queue:
            # Pop the next vertex in line and visit it's neighbors, adding
            # them to the queue if they don't already have a value set in the
            # distance_dict. 
            current = search_queue.pop(0)
            for neighbor in self.graph[current]:
                if neighbor == self.largest:
                    return distances_dict[current] + 1
                if math.isnan(distances_dict[neighbor]):
                    distances_dict[neighbor] = distances_dict[current] + 1
                    search_queue.append(neighbor)

        return float('nan')

    def number_of_paths(self):
        """
        Visits verticies in topological order, adding the count of the paths to
        the current vertex to the count of paths at adjacent verticies. 
        """
        num_paths = [1]
        for i in range(1, self.largest):
            num_paths.append(0)

        for i in range(1, self.largest):
            for j in range(i+1, self.largest+1):
                if j in self.graph[i]:
                    num_paths[j-1] = num_paths[i-1] + num_paths[j-1]
        
        return num_paths[self.largest-1]

    def longest_to_n(self):
        """
        Visits nodes in topological order updating the longest path as it
        goes along. Returns the length of the longest path.
        """
        distances_dict = {n:float('nan') for n in range(1, self.largest+1)}
        distances_dict[1] = 1
        for vertex in range(1, self.largest+1):
            for neighbor in self.graph[vertex]:
                if (math.isnan(distances_dict[neighbor]) or 
                distances_dict[neighbor] <= distances_dict[vertex]):
                    distances_dict[neighbor] = distances_dict[vertex] + 1
                    
        return distances_dict[self.largest-1]


graph = DirectedGraph.read_graph()
print(f'Total paths: {graph.number_of_paths()}')
print(f'Shortest path: {graph.shortest_to_n()}')
print(f'Longest path: {graph.longest_to_n()}')
