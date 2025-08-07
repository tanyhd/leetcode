class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows <= 2:
            return [[1],[1,1]]

        row = Solution.generate(self, numRows-1)
        lastRow = row[-1]

        newRow = [1]
        for i in range(0, len(lastRow)-1):
            newRow.append(lastRow[i] + lastRow[i+1])
        newRow.append(1)
        row.append(newRow)
        return row