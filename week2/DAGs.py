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

class DirectedGraph:
"""
A class for our directed graph. This class takes advantage of the restrictions
on input specified in the file doc string and is not meant for use outside
this script.
"""
    def __init__(N: int)
    '''
