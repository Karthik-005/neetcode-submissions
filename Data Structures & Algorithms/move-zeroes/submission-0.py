class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for r in range(len(nums)):
            if nums[r]:
                nums[r], nums[pos] = nums[pos], nums[r]
                pos += 1