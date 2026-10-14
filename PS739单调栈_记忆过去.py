class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[]
        answer=[0]*len(temperatures)
        for i in range(len(temperatures)-1):
            if not stack or temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
                i+=1
            while stack and temperatures[i]>temperatures[stack[-1]]:
                answer[stack[-1]]=i-stack[-1]
                stack.pop()
        while stack and temperatures[len(temperatures)-1]>temperatures[stack[-1]]:
            answer[stack[-1]]=len(temperatures)-stack[-1]
            stack.pop()
        return answer

if __name__=="__main__":
    s=Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])