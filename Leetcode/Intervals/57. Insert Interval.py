from bisect import bisect_left

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        idx = bisect_left(intervals, newInterval[0], key=lambda item: item[1])
        if idx == len(intervals):
            intervals.append(newInterval)
            return intervals

        ans = []
        for pos, (st, en) in enumerate(intervals):
            if idx == pos:
                ans.append(newInterval)
            if ans and st <= ans[-1][1]:
                ans[-1] = [min(ans[-1][0], st), max(ans[-1][1], en)]
            else:
                ans.append([st, en])
        
        return ans
    
# I think this is more easier to understand/write
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        idx = bisect_left(intervals, newInterval)
        intervals = intervals[:idx] + [newInterval] + intervals[idx:]

        ans, i = [], 0
        while i < len(intervals):
            if not ans:
                ans.append(intervals[i])
            else:
                st, en = ans[-1]
                if st <= intervals[i][0] <= en:
                    en = max(en, intervals[i][1])
                    ans[-1] = [st, en]
                else:
                    ans.append(intervals[i])
                i += 1
        return ans
