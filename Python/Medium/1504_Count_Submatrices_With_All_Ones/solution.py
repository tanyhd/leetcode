class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r-1 >= 0 and mat[r][c] != 0:
                    mat[r][c] += mat[r-1][c]
        count = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    continue 
                
                minRCount = float('inf')
                for k in range(c, -1, -1):
                    if mat[r][k] == 0:
                        break
                    minRCount = min(minRCount, mat[r][k])
                    count += minRCount

        return count
        