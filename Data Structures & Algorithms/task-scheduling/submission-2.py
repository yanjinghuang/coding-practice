from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # optimal to do the max freq task first - > max heap 

        time = 0
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # count, time_finshed

        while maxHeap or q:
            time += 1 

            if maxHeap: 
                cnt = heapq.heappop(maxHeap) + 1 
                if cnt!= 0:
                    q.append([cnt, time + n])

            else:   # no working item
                time = q[0][1]
            
            if q and q[0][1] == time:  #finished 
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time 
