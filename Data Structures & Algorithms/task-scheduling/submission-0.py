class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequency in hashmap
        # push everything onto maxHeap and store: task, count 
        #while heap and queue not empty
        # move any task whose cooldown expired from queue -> heap
        # if heap has something that is not in Q: pop, execute, dec count, if count >0 push into cooldown with readyTime = time + n + 1
        # else: idle
        # time++
        
# time = 4
# maxHeap: x:0, y:0
# PQ:
        
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])


        return time

