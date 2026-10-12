import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # optimal to do the max freq task first - > max heap 

        time = 0 

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque() # [remaing task count, time]


        while maxHeap or q:
            time += 1
            if maxHeap: # to be worked 
                cnt = heapq.heappop(maxHeap) + 1  # = decrement by 1
                if cnt != 0:
                    q.append([cnt, time + n])
            
            else:
                time = q[0][1] # advance to time when it is relases

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # insert remaing count
        
        return time 


       