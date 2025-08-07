class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        main = ""
        sub = ""
        mainPoint = 0
        subPoint = 0
        if x > y:
            main = "ab"
            sub = "ba"
            mainPoint = x
            subPoint = y
        else:
            main = "ba"
            sub = "ab"
            mainPoint = y
            subPoint = x
        
        stack1 = []
        #first pass
        for i in range (0, len(s)):
            c = s[i]
            if len(stack1) != 0 and stack1[-1] + c == main:
                stack1.pop()
            else:
                stack1.append(c)
        
        points = ((len(s) - len(stack1)) // 2) * mainPoint

        #second pass
        stack2 = []
        for i in range(len(stack1)):
            c = stack1[i]
            if len(stack2) != 0 and stack2[-1] + c == sub:
                stack2.pop()
            else:
                stack2.append(c)
        
        points += ((len(stack1)-len(stack2)) // 2) * subPoint

        return points
        
