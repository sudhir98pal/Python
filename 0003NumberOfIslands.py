class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        def isSafe(x,y)->bool:
            return x>=0 and x<n and y>=0 and y<m
        ans=0
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        def dfs(x,y):
            if isSafe(x,y)==False or grid[x][y]=='0':
                return
            grid[x][y]='0'
            nx,ny=0,0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                dfs(nx,ny)
                
            return
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans=ans+1
        return ans            
                
        
