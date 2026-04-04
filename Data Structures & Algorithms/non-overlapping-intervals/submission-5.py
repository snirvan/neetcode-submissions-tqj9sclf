class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # [1,4], [3,5], [5,7], [6,9]
        # [1,5] [5,9]

        # sort intervals
        og_intervals_len = len(intervals)
        intervals =  sorted(intervals, key = lambda x:x[0])

        results = []
        results.append(intervals[0])
        lastEnd = results[-1][1]

        results_len = 1
        print(intervals)
        for i in range(1,len(intervals)):
            print("lastEnd: " + str(lastEnd) + ", current index " + str(i) + ": " + str(intervals[i]))
            if intervals[i][0] < lastEnd:
                results[-1][1] = min(lastEnd, intervals[i][1])
                print("revise")
            else:
                results.append(intervals[i])
                results_len += 1
                print("appending at index" + str(i) + str(intervals[i]))
            lastEnd = results[-1][1]

        print(results)
        return og_intervals_len - results_len

# [1,2], [2,4], [1,4]
# lastEnd = 4
# results: [1,2], [2,4]