"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        intervals = sorted(intervals, key = lambda x: x.start)

        # results = []

        # results.append(intervals[0])

        # lastEnd = results[-1].end
        # results_len = 1
        # for i in range(1,len(intervals)):
        #     if intervals[i].end < lastEnd:
        #         results[-1].end = min(lastEnd, intervals[i].end)
        #     else:
        #         results.append(intervals[i])
        #         results_len += 1
        #     lastEnd = results[-1].end
        
        # return results_len

        # rooms = 1
        # minheap
        # take current interval, if next interval startTime >= last Endtime: continue
        # else:
            # add room
        # update lastEnd

        heap = []
        rooms = 1
        for interval in intervals:
            if heap:
                if interval.start >= heap[0]:
                    heapq.heappop(heap)
                else:
                    rooms += 1
            
            heapq.heappush(heap,interval.end)
            
        return rooms