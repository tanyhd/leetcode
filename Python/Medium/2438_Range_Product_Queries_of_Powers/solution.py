class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        bNum = bin(n)
        powers = []

        bCount = 0
        for i in range(len(bNum)-1, 0, -1):
            if bNum[i] == "b":
                break
            if bNum[i] == "0":
                bCount += 1
                continue
            powers.append(2**bCount)
            bCount += 1

        output = []
        mod = 10**9 + 7
        for q in queries:
            start, stop = q
            count = 1
            for i in range(start, stop + 1):
                count *= powers[i]
            count = count % mod
            output.append(count)
        return output