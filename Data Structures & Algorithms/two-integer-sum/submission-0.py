class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force, O(n^2), O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        """

        # Hash Map (One Pass) O(n), O(n)
        lookup_map = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup_map:
                # return the index of what is stored and the curr inx
                return [lookup_map[diff],i]
            # Otherwise store index at location n
            lookup_map[n] = i



        