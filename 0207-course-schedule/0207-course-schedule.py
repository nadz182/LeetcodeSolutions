class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedList = []
        
        if numCourses <= 0:
            return False
        
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)} 
        
        for pre in prerequisites:
            parent, child = pre[0], pre[1]
            graph[parent].append(child)
            inDegree[child] += 1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            vertix = sources.popleft()
            sortedList.append(vertix)
            
            for child in graph[vertix]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return len(sortedList) == numCourses