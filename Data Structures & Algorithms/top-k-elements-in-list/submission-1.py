class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for x in nums:
            seen[x] = seen.get(x, 0) + 1
        return sorted(seen, key=seen.get, reverse=True)[:k]