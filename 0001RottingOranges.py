class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans=0
        n,m=len(grid),len(grid[0])
        q=[]
        fresh=0
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        def isSafe(x,y):
            return (x>=0 and x<n and y>=0 and y<m)
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    fresh=fresh+1
                if(grid[i][j]==2):
                    q.append(i)
                    q.append(j)
        if fresh==0:
            return 0
        while len(q)>0:
            c=int(len(q)/2)
          
            if(fresh<=0):
                return ans
            ans=ans+1
            while c>0:
                c=c-1
                x=q.pop(0)
                y=q.pop(0)
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if(isSafe(nx,ny)):
                        if(grid[nx][ny]==1):
                            fresh=fresh-1
                            grid[nx][ny]=2
                            q.append(nx)
                            q.append(ny)
           
        if(fresh>0):
            return -1;
        return ans              
                        
                
                
        
