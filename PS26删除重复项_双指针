class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left=0
        right=0
        while right<len(nums):
            if nums[right]==nums[left]:
                right+=1
            else:
                left+=1
                nums[left]=nums[right]
                right+=1
        # print(nums)
        # print(left+1)
        return left+1

s=Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
