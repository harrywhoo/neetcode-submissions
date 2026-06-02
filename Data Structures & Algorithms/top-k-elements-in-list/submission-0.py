import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)] # frequencies can 1 to len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1 

        for num in freq:
            buckets[freq[num]].append(num)

        res = []
        i = len(nums)
        while len(res) < k:
            bucket = buckets[i]
            for j in range(len(bucket)):
                res.append(bucket[j])
                if len(res) == k:
                    return res 
            i -= 1 
    
        return res 