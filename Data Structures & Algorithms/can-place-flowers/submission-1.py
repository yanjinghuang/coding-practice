class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        empty = 1

        for f in flowerbed:
            if f == 0:
                empty += 1 
            else:
                n -= int((empty - 1) / 2)
                empty = 0
        
        n -= empty // 2 

        return n <= 0 
                


        