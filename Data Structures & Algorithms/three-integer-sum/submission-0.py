class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)) :
            if i != 0 and nums[i-1] == nums[i] :
                continue

            left, right = i+1, len(nums)-1
            while left < right :
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 < 0 :
                    left += 1

                elif sum3 > 0:
                    right -= 1

                else :
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Understand why this while should stay inside the else condition and not outside, submit it in both cases and 
                    #manually check the reaosn.
                    while left < right and nums[left-1] == nums[left] :
                        left += 1

        return res         