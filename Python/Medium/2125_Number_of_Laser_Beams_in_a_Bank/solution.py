class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        bankArray = []

        for r in range(len(bank)):
            count = 0
            for c in range(len(bank[0])):
                if bank[r][c] == "1":
                    count += 1
            if count != 0:
                bankArray.append(count)

        total = 0
        for i in range(len(bankArray)-1):
            total += bankArray[i] * bankArray[i+1]
        return total