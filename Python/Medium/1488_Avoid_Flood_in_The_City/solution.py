import bisect

class Solution:
    def avoidFlood(self, rains: list[int]) -> list[int]:
        output = [1] * len(rains)
        lastWetDay = {}
        dryDays = []
        
        for i in range(len(rains)):
            lake = rains[i]
            if lake == 0:
                dryDays.append(i)
            else:
                output[i] = -1

                if lake in lastWetDay:
                    dryDayIndex = bisect.bisect_right(dryDays, lastWetDay[lake])
                    if dryDayIndex == len(dryDays):
                        return []
                    d = dryDays.pop(dryDayIndex)
                    output[d] = lake
                lastWetDay[lake] = i
        return output