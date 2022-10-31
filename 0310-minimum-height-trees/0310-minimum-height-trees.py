class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<= 0:
            return []
        if n==1:
            return [0]
        
        inDegree = {i: 0 for i in range(n)}
        graph = {i: [] for i in range(n)}
        
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            inDegree[n1] += 1
            inDegree[n2] += 1
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        leaves = deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leaves.append(key)
        
        totalNodes = n
        while totalNodes > 2:
            leaveSize = len(leaves)
            totalNodes -= leaveSize
            
            for i in range(0, leaveSize):
                v = leaves.popleft()
                for child in graph[v]:
                    inDegree[child] -=1
                    if inDegree[child] == 1:
                        leaves.append(child)
        return list(leaves)