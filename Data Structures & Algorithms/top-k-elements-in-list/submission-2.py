class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []

        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result