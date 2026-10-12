class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        ans=[]
        i=0
        cur=intervals[0]
        for i in range(len(intervals)-1):
            next=intervals[i+1]
            if cur[1]>=next[0]:
                cur[1]=max(next[1],cur[1])
                next=intervals[i+1]
            else:
                ans.append(cur)
                cur=next
            i+=1
        ans.append(cur)
        return ans

if __name__ == '__main__':
    s=Solution()
    s.merge([[1,3],[2,4]])

            
