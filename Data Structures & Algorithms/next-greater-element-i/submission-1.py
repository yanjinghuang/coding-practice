class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # monotonic stack -> linear time O(n+m)
        # stack: pending 
        # hashmap: store found  element : next greater element

        hm = {}
        stack = [] 

        for x in nums2:
            while stack and x > stack[-1]:
                hm[stack.pop()] = x 
            
            stack.append(x)

        return [hm.get(x, -1) for x in nums1]