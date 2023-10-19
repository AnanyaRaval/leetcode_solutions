
#https://leetcode.com/problems/detonate-the-maximum-bombs/

from typing import List
from collections import defaultdict, Counter

"""
TECHNIQUE: DFS. Directed graph problem.
PROCEDURE: 
1. Create a loop with index i to go over all the bomb coordinates:
    1.1 Create a nested for loop with index j to go over all the bomb coordinates:
        1.1.1 If it is the same bomb index, ignore and continue the loop.
        1.1.2 Unpack bomb coordinates for bombs[i].
        1.1.3 Check if bombs[j] is within the circle of bombs[i].
            => There is a directed edge between bombs[i] -> bombs[j].
        1.1.4 Add bombs[j] as a neighbour in the adj list of bombs[i].
2. Initialize a variable result to store the maximum number of bombs exploded.
3. Create a counter of bombs. This denotes the number of bombs at the same coordinate and with the same radius.
4. Create a for loop to traverse through bombs => This denotes the bomb which starts the explosion.
    3.1 Initialize a visited set to keep track of visited bombs.
    3.2 Call dfs() which traverses through all the neighbors and returns the number of bombs exploded.
    3.3 Calculate the maximum of current explosions and result.
5. Return result
DFS:
1. Create a function with 3 parameters: x, y and r as given in the input.
2. Add the bomb coordinate in the visited set.
3. Create a local variable curr and add bomb_counter for the argument.
    This adds the number of bombs which exploded at this coordinate.
4. For every neighboring bomb in the adjacency list, recurse dfs and add the return value to curr.
5. Return the curr variable. This stores the total number of bombs exploded.
IN_CIRCLE:
1. Create a function with 5 parameters: x,y,r, n_new, y_new.
2. Initialize the variable dx to (x - x_new) ** 2 to find the Euclidean dist between x coordinates.
3. Initialize the variable dy to (y - y_new) ** 2 to  find the Euclidean dist between y coordinates.
4. Return if dx + dy is <= r ** 2. This condition shows that the coordinate x_new, y_new 
    is within the circle denoted by x, y and radius r.
TIME COMPLEXITY: O(n^3). O(n^2) for graph creation. O(n) * O(n^2) for dfs on every node.
SPACE COMPLEXITY: O(n^2). O(n^2) for adjacency list. O(n) for stack space. 
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(x:int, y:int, r:int):
            visited.add((x,y,r))
            curr = bomb_counter[(x,y,r)]
            for neigh in graph[(x,y,r)]:
                if neigh not in visited:
                    curr += dfs(neigh[0], neigh[1], neigh[2])
            return curr        
        
        def in_circle(x:int, y:int, r:int, x_new:int, y_new:int) -> bool:
            dx = (x_new - x) ** 2
            dy = (y_new - y) ** 2
            return dx + dy <= r ** 2

        graph = defaultdict(list)
        for i in range(len(bombs)):
            x, y, r = bombs[i]
            for j in range(len(bombs)):
                if j == i:
                    continue
                x_n,y_n,r_n = bombs[j]
                if in_circle(x,y,r,x_n,y_n):
                    graph[(x,y,r)].append((x_n,y_n,r_n))
        
        result = 0
        bomb_counter = Counter([tuple(bomb) for bomb in bombs])
        for x,y,r in bombs:
            visited = set()
            result = max(result,dfs(x,y,r))
        return result
        
"""
Cleaner version of the above code.

-> Can we reduce the space for adjacency list?
Yes. We can store indices instead of (x,y,r) tuple given in the input.
This way we do not need to create a counter as the indices are unique and two bombs
at the same place will be considered separate in the DFS call stack.
-> We clean up the dfs function: Remove the curr variable for counting the bombs and
use size visited set to count the max. number of explosions.
TIME COMPLEXITY: O(n^3)
SPACE COMPLEXITY: O(n^2)
"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node:int, visited:set) -> int:
            visited.add(node)
            for neighb in graph[node]:
                if neighb not in visited:
                    dfs(neighb, visited)
            return len(visited)

        def in_circle(s:int, d:int) -> bool:
            x, y, r = bombs[s]
            x_n, y_n, _ = bombs[d]
            return (x-x_n) ** 2 + (y-y_n) ** 2 <= r ** 2

        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue
                if in_circle(i,j):
                    graph[i].append(j)
        
        result = 1
        for i in range(len(bombs)):
            visited = set()
            result = max(result, dfs(i, visited))
        return result
        