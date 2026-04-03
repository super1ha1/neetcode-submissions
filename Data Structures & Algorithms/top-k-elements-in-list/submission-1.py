class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        sort_map = dict(sorted(m.items(), key=lambda x: x[1], reverse=True))
        print(sort_map)
        print(sort_map.keys())
        return list(sort_map.keys())[:k]