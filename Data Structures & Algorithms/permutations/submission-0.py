class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def func(seen=set(), l=[]):
            if len(l) == len(nums):
                res.append(l)
                return

            for i in range(len(nums)):
                if nums[i] in seen:
                    continue

                seen.add(nums[i])
                new_l = l.copy()
                new_l.append(nums[i])
                func(seen, new_l)
                seen.remove(nums[i])
        

        func()
        return res