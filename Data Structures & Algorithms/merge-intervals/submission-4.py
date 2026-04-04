class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        # if interval[i][1] < interval[i+1][0]: 
        #     continue
        # if interval[i][0] > intervals[i+1][1]:
        #     continue
        # else: overalpping --> merge
        #     mergedInterval = [min(interval[i][0], interval[i+1][0]), max(interval[i][1], interval[i+1][1])]
        #     remove indexes: i and i+1
        #     insert mergedInterval at index i

        results = []
        results.append(intervals[0])
        lastEnd = results[-1][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= lastEnd:
                results[-1][1] = max(lastEnd, intervals[i][1])
            else:
                results.append(intervals[i])
            lastEnd = results[-1][1]
        # i = 0 
        # while i+1 < len(intervals):
        #     print(i)
        #     if intervals[i][1] < intervals[i+1][0]:
        #         i = i + 1
        #         results.append(intervals[i])
        #         continue
        #     if intervals[i][0] > intervals[i+1][1]:
        #         i = i+1
        #         results.append(intervals[i])
        #         continue
        #     else:
        #         mergedInterval = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
        #         # intervals.pop(i)
        #         # intervals.pop(i)
        #         # intervals.insert(i,mergedInterval)
        #         # newInterval = intervals[:i]
        #         # newInterval.append(mergedInterval)
        #         # newInterval.extend(intervals[i+2:])
        #         # intervals = newInterval
        #         results.append(mergedInterval)
        #         i = i + 2
        #     print(intervals)
        return results



        # i = 1
        # len(intervals) = 2
        # i + 1 < len(intervals)

        # [1,5], [6,7]