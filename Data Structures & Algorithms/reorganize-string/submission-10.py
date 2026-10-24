class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in count.items()]
        heapq.heapify(maxHeap)
    
        res = ""
        held = None
        

        while maxHeap or held:
            if held and not maxHeap:
                return ""      
            cnt, c = heapq.heappop(maxHeap)
            res += c
            cnt += 1 

            if held:
                heapq.heappush(maxHeap, held)
                held = None
            
            if cnt!= 0:
                held = [cnt,c]
    

        return res

                
            
            
            