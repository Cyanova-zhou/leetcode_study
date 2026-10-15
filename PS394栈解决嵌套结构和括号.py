class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char=='[':
                stack.append(num)
                stack.append(char)
                num=0
            elif char==']':
                cash_list=[]
                while stack[-1]!='[':
                    cash_list.append(stack[-1])
                    stack.pop()
                cash_list.reverse()
                stack.pop()
                repeat_num=stack.pop()
                stack.append("".join(cash_list)*repeat_num)
            else:
                stack.append(char)
        return "".join(stack)

if __name__=="__main__":
    s=Solution()
    s.decodeString("3[a2[c]]")

