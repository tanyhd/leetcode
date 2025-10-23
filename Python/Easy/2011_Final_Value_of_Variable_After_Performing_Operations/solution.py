class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        opValue = {"--X":-1, "X--":-1, "++X":1, "X++":1}
        x = 0

        for op in operations:
            x += opValue[op]
        
        return x