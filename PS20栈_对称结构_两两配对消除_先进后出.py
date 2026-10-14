class Solution:
    def isValid(self, s: str) -> bool:
        pair={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i in pair:
                stack.append(i)
            elif stack:
                if i==pair[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                    return False

            # 8-14可以简化为
            # elif stack and i == pair[stack[-1]]:
            #     stack.pop()
            # else:
            #     return False

        if stack:
            return False
        else:
            return True

s=Solution()
s.isValid("()")





