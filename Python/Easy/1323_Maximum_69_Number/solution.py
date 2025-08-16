class Solution:
    def maximum69Number (self, num: int) -> int:
        output = ""
        num = str(num)
        for i in range(len(num)):
            if num[i] == "6":
                output += "9"
                if i < len(num) - 1:
                    output += num[i+1:]
                break
            else:
                output += num[i]
        return int(output)