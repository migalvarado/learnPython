'''
http://community.topcoder.com/stat?c=problem_statement&pm=13793

Problem can be solved using Dijkstra's algorithm
Created on May 16, 2015

@author: mig
'''
from copy import deepcopy
import heapq

NODE_NUM_INDEX = 0
R_INDEX = 1
C_INDEX = 2

def minimumLongestDistance(R, C):
    G = buildGraph(R, C)
    V = G.keys()
    
    smallestMaximumDistance = -1
    
    # Iterate over every possible teleporter pairing
    for t1 in V:
        for t2 in V:
            maximumDistance = 0
            
            # For this particular teleporter pairing, iterate over all cells
            for v in V:
                thisMax = getMaxDistance(v, G, t1, t2, R, C)
                
                if thisMax > maximumDistance:
                    maximumDistance = thisMax
                    
            if maximumDistance < smallestMaximumDistance or smallestMaximumDistance == -1:
                smallestMaximumDistance = maximumDistance
                
    print(smallestMaximumDistance)
    
def buildGraph(R, C):
    V = [(r, c) for r in range(R) for c in range(C)]
    V = [((i,) + v) for i, v in enumerate(V)] # Not necessary, but add numbering to cells
    E = []
    
    for i, v in enumerate(V):
        # Each possible neighbor is directly to the left, right, below, and
        # above, respecting the grid boundaries
        neighbors = [(i + r*C + c, r + v[R_INDEX], c + v[C_INDEX])
                     for (r, c) in ((-1, 0), (1, 0), (0, -1), (0, 1))
                     if r + v[R_INDEX] not in (-1, R) and c + v[C_INDEX] not in (-1, C)]
        
        E.append(neighbors)
        
    G = dict(zip(V, E));
    
    return G

def getMaxDistance(s, G, t1, t2, R, C):
    #print(s, G, t1, t2)
    maxDistance = 0;
    myG = deepcopy(G)
    
    grid = [[0 for c in range(C)] for r in range(R)]
    
    # Append the t1 teleporter location to t2's neighbors list
    t1Neighbors = myG[t1]
    
    if t2 not in t1Neighbors:
        t1Neighbors.append(t2)
        
    # Append the t2 teleporter location to t1's neighbors list
    t2Neighbors = myG[t2]
    
    if t1 not in t2Neighbors:
        t2Neighbors.append(t1)
    
    distances = [0 for x in range(len(G.keys()))]
    visited = [False for x in range(len(distances))]
    visited[s[NODE_NUM_INDEX]] = True
    
    q = [(0, s)]
    
    while len(q) > 0:
        (vd, v) = heapq.heappop(q)
        
        neighbors = myG[v]
        
        if len(neighbors) > 0: # Must have neighbors to potentially add to q
            minDistance = -1
            
            for n in neighbors: # Iterate over neighbors
                ni = n[NODE_NUM_INDEX]
                
                if not visited[ni]: # This node has not been discovered yet
                    nd = vd;
                    
                    if n not in (t1, t2):
                        nd += 1
                        
                    if nd < minDistance or minDistance == -1: # New min distance
                        m = n
                        minDistance = nd
                        
            if minDistance > -1: # Verify at least one new neighbor found
                visited[m[NODE_NUM_INDEX]] = True
                distances[m[NODE_NUM_INDEX]] = minDistance
                grid[m[R_INDEX]][m[C_INDEX]] = minDistance
                
                if minDistance > maxDistance: # Change to new max if applicable
                    maxDistance = minDistance
                    
                # Add the neighbor to the queue
                heapq.heappush(q, (minDistance, m))

    print('Source cell: {}'.format(s))
    print('Teleporter 1: {}'.format(t1))
    print('Teleporter 2: {}'.format(t2))
    for r in range(R):
        print(grid[r])
    print()
    print('Max distance: {}'.format(maxDistance))
    print()
    
    return maxDistance

minimumLongestDistance(4, 1)
minimumLongestDistance(2, 2)
minimumLongestDistance(5, 3)
minimumLongestDistance(8, 2)