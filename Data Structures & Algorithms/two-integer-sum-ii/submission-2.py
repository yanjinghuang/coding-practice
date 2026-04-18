class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 # if sum too small, increment
        j = len(numbers) - 1 # if sum to big, decrement

        while i < j:
            if (numbers[i] + numbers[j]) >  target:
                j -= 1
            elif (numbers[i] + numbers[j]) < target:
                i += 1
            else:
                return [i+1,j+1]
            

        