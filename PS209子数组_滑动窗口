class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        length=float("inf")
        # left=-1
        # right=-1
        # sum=0
        # while right<len(nums)-1 or sum>=target:
        #     if sum<target:
        #         right+=1
        #         sum+=nums[right]
        #     elif sum>=target:
        #         length=min(length,right-left)
        #         left+=1
        #         sum-=nums[left]
        # if length==float("inf"):
        #     return 0
        # else:
        #     return length
        left=0
        right=0
        sum=0
        while right<len(nums):
            sum+=nums[right]
            while sum>=target:
                length=min(length,right-left+1)
                sum-=nums[left]
                left+=1
            right+=1
        if length==float("inf"):
            return 0
        else:
            return length


s=Solution()
s.minSubArrayLen(7,[2,3,1,2,4,3])