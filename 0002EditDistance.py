class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if(word1==word2):
            return 0
        n,m=len(word1),len(word2)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        
        def dfs(word1: str, word2: str,f:int,s:int)->int:
            if(f==0):
                dp[f][s]=s
                return s
            if(s==0):
                dp[f][s]=f
                return f
            if(dp[f][s]!=-1):
                return dp[f][s]
            if(word1[f-1]==word2[s-1]):
                dp[f][s]=(dfs(word1,word2,f-1,s-1))
                return dp[f][s]
            dp[f][s]=1+min(dfs(word1,word2,f-1,s),
                     dfs(word1,word2,f,s-1),dfs(word1,word2,f-1,s-1))
            return dp[f][s]
        return dfs(word1,word2,n,m)
        
        
        
        
        
