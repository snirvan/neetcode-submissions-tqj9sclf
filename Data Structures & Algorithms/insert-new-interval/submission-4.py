class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = []
        overlapping = []
        after = []

        for i in range(len(intervals)):
            # if newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1] or newInterval[1] >= intervals[i][0] and newInterval[1] <= intervals[i][1]:
            #     overlapping.append(intervals[i])

            # elif newInterval[0] > intervals[i][1]:
            #     before.append(intervals[i])
            # else:
            #     after.append(intervals[i])

            if newInterval[1] < intervals[i][0]:
                after.append(intervals[i])
            elif newInterval[0] > intervals[i][1]:
                before.append(intervals[i])
            else:
                overlapping.append(intervals[i])
            

        # print("before:" + str(before))
        # print("overlapping:" + str(overlapping))
        # print("after:" + str(after))

        if len(overlapping) == 0:
            merged_interval = newInterval
        else:
            merged_interval = [min(overlapping[0][0], newInterval[0]), max(overlapping[-1][1],newInterval[1])]


        print("before:" + str(before))
        print("overlapping:" + str(overlapping))
        print("after:" + str(after))

        before.append(merged_interval)
        for i in range(len(after)):
            before.append(after[i])

        return before

