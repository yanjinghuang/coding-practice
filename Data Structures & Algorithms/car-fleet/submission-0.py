class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # t = (target - position) / s. 
        # 1. sorted it by position 2. one pass  O(nlogn)

      
        pairs = sorted(zip(position,speed), reverse = True)

        fleet = 0
        fleet_time = 0.0

        for p, s in pairs:
            t = (target - p) / s
            if t > fleet_time: # longer
                fleet += 1 
                fleet_time = t # can't pass
            
        return fleet 

