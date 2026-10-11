class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)  ##不要减一才能符合左开右闭
        mid=(left+right)//2
        while left<right:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1    ##注意这个加一，因为是左开右闭，左边的这个已经判断过了，不加一可能会卡住
                mid=(left+right)//2
            else:
                right=mid
                mid=(left+right)//2
        return -1