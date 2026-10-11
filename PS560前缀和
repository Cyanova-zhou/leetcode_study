from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=[0]*len(nums)
        sum[0]=nums[0]
        for i in range(1,len(nums)):
            sum[i]=sum[i-1]+nums[i]
        count=0
        cash = {0: 1}
        for item in sum:
            count+=cash.get(item-k,0)
            cash[item]=cash.get(item,0)+1
        return count


s=Solution()
s.subarraySum([1,2,3],3)