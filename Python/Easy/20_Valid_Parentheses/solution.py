class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for c in s:
            if c == ")":
                check = brackets.pop()
                if check != "(":
                    return False
            elif c == "]":
                check = brackets.pop()
                if check != "[":
                    return False
            elif c == "}":
                check = brackets.pop()
                if check != "{":
                    return False
            else:
                brackets.append(c)
        if len(brackets) != 0:
            return False
        return True
