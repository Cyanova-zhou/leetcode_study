class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i=0
        while i <len(nums):
            if nums[i]==i+1 and i<len(nums)-1:
                i+=1
            else:
                if 1<=nums[i]<=len(nums) and nums[i]!=nums[nums[i]-1]:
                    num=nums[i]
                    nums[i],nums[num-1]=nums[num-1],nums[i]
                else:
                    i+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1



if __name__=="__main__":
    s=Solution()
    s.firstMissingPositive([3,4,-1,1])
