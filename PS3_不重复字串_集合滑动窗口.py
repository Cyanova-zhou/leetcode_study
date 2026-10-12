class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cash=set()
        left=0
        right=0
        length=0
        while right<len(s):
            if s[right] in cash:
                cash.remove(s[left])
                left+=1
            else:
                cash.add(s[right])
                right+=1
                length=max(length,len(cash))
        return length


'''
类似PS209用while写
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cash = set()
        left = 0
        length = 0

        for right in range(len(s)):
            while s[right] in cash:
                cash.remove(s[left])
                left += 1

            cash.add(s[right])
            length = max(length, len(cash))

        return length
'''



