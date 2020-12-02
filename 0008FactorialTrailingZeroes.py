class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n<5):
            return 0
        five=0
        i=5;
        while(n//i>0):
            five+=n//i
            n=n//i;
        
            
 
      
         
            
        return five     
            
    
            
        
        
