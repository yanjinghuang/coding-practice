class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0 

        l, r = 0, len(people)-1

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1 # get next see if that exceed the limit 
            count += 1
            r -= 1
        return count


        