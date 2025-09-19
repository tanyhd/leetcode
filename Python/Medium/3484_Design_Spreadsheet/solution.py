class Spreadsheet:

    def __init__(self, rows: int):
        self.labeled = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
                   "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"] 
        self.grid = {}
        for i in range(1, rows + 1):
            data = {}
            for col in self.labeled:
                data[col] = 0
            self.grid[i] = data

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        count = 0
        formula = formula[1:]
        values = formula.split("+")
        for value in values:
            if value[0] not in self.labeled:
                count += int(value)
            else:
                col = value[0]
                row = int(value[1:])
                count += self.grid[row][col]
        return count


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)