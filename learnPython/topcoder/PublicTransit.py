'''
http://community.topcoder.com/stat?c=problem_statement&pm=13793

Problem can be solved using Dijkstra's algorithm
Created on May 16, 2015

@author: mig
'''
def minimumLongestDistance(R, C):
    (V, E) = buildGraph(R, C)
    
    
def buildGraph(R, C):
    V = [(x, y) for x in range(R) for y in range(C)]
    E = []
    
    for v in V:
        neighbors = [(x + v[0], y + v[1])
                     for (x, y) in ((-1, 0), (1, 0), (0, -1), (0, 1))
                     if x + v[0] not in (-1, R) and y + v[1] not in (-1, C)]
        
        E.append(neighbors)
        
    return (V, E)

minimumLongestDistance(4, 1)
minimumLongestDistance(2, 2)
minimumLongestDistance(5, 3)
minimumLongestDistance(8, 2)