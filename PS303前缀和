class NumArray:

    def __init__(self, nums: list[int]):
        self.sum=[0]*len(nums)
        self.sum[0]=nums[0]
        for i in range(1,len(nums)):
            self.sum[i]=nums[i]+self.sum[i-1]
        print(self.sum)


    def sumRange(self, left: int, right: int) -> int:
        if left-1>=0:
            return self.sum[right]-self.sum[left-1]
        else:
            return self.sum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)