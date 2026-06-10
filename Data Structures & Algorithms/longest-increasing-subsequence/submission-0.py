class Solution:
    def lengthOfLIS(self, nums):
        seen = [[-1] * len(nums) for _ in range(len(nums)+1)] 

        def func(i, j=-1):
            if i == len(nums):
                return 0

            if seen[i][j] != -1:
                return seen[i][j]

            seen[i][j] = func(i+1, j)

            if (j != -1 and nums[i] > nums[j]) or j == -1:
                seen[i][j] = max(1 + func(i+1, i), seen[i][j])

            return seen[i][j]

        return func(0)