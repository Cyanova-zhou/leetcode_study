class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # output=[[0]*n for _ in range(n)]
        # i=0
        # input=1
        # while input<n*n:
        #     for x in range(i,n-1-i):
        #         output[i][x]=input
        #         input+=1
        #     for x in range(i,n-1-i):
        #         output[x][n-1-i]=input
        #         input+=1
        #     for x in range(n-1-i,i,-1):
        #         output[n-1-i][x]=input
        #         input+=1
        #     for x in range(n-1-i,i,-1):
        #         output[x][i]=input
        #         input+=1
        #     i+=1

        # if n%2==1:
        #     output[n//2][n//2]=n*n

        
        # return output


        top=0
        bottom=n-1
        left=0
        right=n-1
        count=1
        output=[[0]*n for _ in range(n)]
        while count<=n*n:
            for j in range(left,right+1):   ##是撞到墙，所以右边要顶住right，范围是right+1
                output[top][j]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                output[i][right]=count
                count+=1
            right-=1
            for i in range(right,left-1,-1):
                output[bottom][i]=count
                count+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                output[i][left]=count
                count+=1
            left+=1
            
            
        return output


















s=Solution()
s.generateMatrix(4)

    