class Solution:
    def makeFancyString(self, s: str) -> str:
        output = [s[0]]
        count = 1
        for i in range(1, len(s)):
            c = s[i]
            if c != output[-1]:
                output.append(c)
                count = 1
            else:
                if count >= 2:
                    continue
                else:
                    count += 1
                    output.append(c)
        return "".join(output)

