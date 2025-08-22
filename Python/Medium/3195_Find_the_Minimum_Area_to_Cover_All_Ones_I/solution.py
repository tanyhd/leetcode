class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        start = False
        pos = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if not start:
                        pos.append(r)
                        pos.append(c)
                        pos.append(c)
                        pos.append(r)
                        start = True
                    else:
                        tr = pos[0]
                        if r < tr:
                            pos[0] = r

                        lc = pos[1]
                        if c < lc:
                            pos[1] = c

                        rc = pos[2]
                        if c > rc:
                            pos[2] = c

                        br = pos[3]
                        if r > br:
                            pos[3] = r
    
        height = pos[3] - pos[0] + 1 
        width = pos[2] - pos[1] + 1
        return height * width