class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogn) Solution 
        # res = defaultdict(int) # {n: count}

        # for n in nums:
        #     res[n] += 1
        # # sorted the keys by the values of the key in a reversed order
        # sorted_keys = sorted(res.keys(), key=lambda x : res[x], resversed = True)
        # return list(sorted_keys[:k])

        # O(n) solution using Bucket sort - the dict will be the same size of the nums
        # Using {count:[num]} -> get the num append to the list from right to left for k steps

        # count = {} # {n:count}
        # freq = [[] for i in range(len(nums)+1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # for n, c in count.items():
        #     freq[c].append(n)
        
        # # reverse the frequency array and return the most frequent values
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


        # Practice 
        # bucket sort 

        freq = [[] for i in range(len(nums)+1)] # list of list, indicies = count; no need to sort also len is the len(n)
        counts = {}  #{n: count}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        for n, c in counts.items():
            freq[c].append(n)
        
        # Iterate in a reversed order to get top k items 
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



    


    


            




