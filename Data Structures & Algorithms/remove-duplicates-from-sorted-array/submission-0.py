class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        k = 0
        for j in range(1, len(nums)):
            if nums[k] != nums[j]:
                k += 1
                nums[k] = nums[j]
        return k + 1 