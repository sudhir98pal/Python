class maxSubArrayLengthWithSumEqualToZero:
    def maxLength(self, arr) -> int:
        n=len(arr)
        maxLen=0
        map={}
        currentSum=0
        for i in range(n):
            currentSum=currentSum+arr[i]
            if(arr[i]==0 and maxLen==0):
                maxLen=1
            if(currentSum==0):
                maxLen=i+1
            if(currentSum in map):
                maxLen=max(maxLen,i-map[currentSum])
            else:
                map[currentSum]=i            
        return maxLen

t=10
while t>0:
    t=t-1
    arr=[int(x) for x in input().split()]
    sudhir=maxSubArrayLengthWithSumEqualToZero()
    x=sudhir.maxLength(arr)
    print(x)
