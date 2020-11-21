class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if(len(prerequisites)==0):
            return True
        indegree=[0 for i in range(numCourses)]
        ans=0
        q=[]
        graph=defaultdict(list)
        for x in prerequisites:
            indegree[x[0]]=indegree[x[0]]+1
            graph[x[1]].append(x[0])
        for i, node in enumerate(indegree):
            if node == 0:
                q.append(i)
         
      
        while(len(q)>0):
            front=q.pop(0)
            ans=ans+1
            for adjacent in graph[front]:
                indegree[adjacent]=indegree[adjacent]-1
                if(indegree[adjacent]==0):
                    q.append(adjacent)
            
            
        
        return ans==numCourses
        
