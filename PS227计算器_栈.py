class Solution:
    def calculate(self, s: str) -> int:
        pre_sign = "+"
        num = 0
        stack = []
        s = s.replace(" ", "")
        for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i]) + num * 10
            if not s[i].isdigit() or i==len(s)-1:
                if pre_sign == "+":
                    stack.append(num)
                    num=0
                    pre_sign = s[i]
                elif pre_sign == "-":
                    stack.append(-num)
                    num=0
                    pre_sign = s[i]
                elif pre_sign == "*":
                    stack.append(stack.pop()*num)
                    num=0
                    pre_sign = s[i]
                elif pre_sign == "/":
                    stack.append(int(stack.pop()/num))
                    num=0
                    pre_sign = s[i]
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    s.calculate("3+2*2")
