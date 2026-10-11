class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # cash={}
        # for i,item in enumerate(nums):
        #     cash[item]=i
        # for i in range(len(nums)):
        #     if (target-nums[i]) in cash and i !=cash[target-nums[i]]:
        #         print([i,cash[target-nums[i]]])
        #         return [i,cash[target-nums[i]]]
        cash={}
        for i,item in enumerate(nums):
            if (target-item) in cash:
                return [cash[target-item],i]
            cash[item]=i

s=Solution()
s.twoSum([1,3,4,3],6)


'''
这样子写字典中可能会覆盖已经记录过的数组中重复的数
例如[1,3,1] 其中字典中1储存的只剩2
但是不会影响这道题目的解答
因为第一次出现是通过nums的下标实现的
更好地做法是边遍历边存入
'''