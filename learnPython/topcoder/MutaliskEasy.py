'''
http://community.topcoder.com/stat?c=problem_statement&pm=13782

Created on May 17, 2015

@author: mig
'''
from itertools import permutations

def minimalAttacks(x):
    x.sort(reverse=True)
    hps = [0 for x in range(len(x))]
    isFull = [False for x in range(len(x))]
    numAttacks = 0
    aps = [9, 3, 1]
    nextAps = [1, 2, -1]
    
    while isFull.count(True) < len(x):
        for i in range(len(x)):
            isOverkill = hps[i] + aps[i] > x[i]
            while isOverkill and nextAps[i] != -1: # current ap is overkill, see if next lowest can still get the job done
                    
                    aps[i], aps[nextAps[i]] = aps[nextAps[i]], aps[i]
                    if i + 1 == nextAps[i]:
                        temp = nextAps[i]
                        
                        nextAps[i] = nextAps[temp]
                        nextAps[temp] = temp - 1
                    else:  
                        nextAps[i], nextAps[nextAps[i]] = nextAps[nextAps[i]], nextAps[i]
                    isOverkill = hps[i] + aps[i] > x[i]
            
            hps[i] += aps[i]
            
            isFull[i] |= hps[i] >= x[i]
        
        numAttacks += 1
    
    
#     done = False;
#     
#     while not done:
#         minimumWaste = -1;
#         minimumPerm = ()
#         
#         for perm in permutations(len(x)):            
#             results = [currentHp[p] + (3 ** (2 - i)) for i, p in enumerate(perm)]
#             
#             waste = [max(0, results[i] - x[p[i]]) for i in len(x)]
#             
#             totalWaste = sum(waste)
#             
#             if totalWaste < minimumWaste or minimumWaste == -1:
#                 minimumWaste = totalWaste
#                 minimumPerm = perm
#                 
#         for i, p in minimumPerm:
#             currentHp[p] += 3 ** (2 - i)
            
        
    print(numAttacks)
    
minimalAttacks([12, 10, 4])
minimalAttacks([54, 18, 6])
minimalAttacks([55, 60, 53])
minimalAttacks([1, 1, 1])
minimalAttacks([60, 40])
minimalAttacks([60])