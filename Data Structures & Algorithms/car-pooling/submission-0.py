class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        event = [] 

        for n, f, t in trips:
            event.append((f, n))
            event.append((t, -n))
        event.sort()


        cur = 0 
        for location, number in event:
            cur += number 
            if cur > capacity:
                return False
        return True


 
         