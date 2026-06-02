from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        result = [i[0] for i in count.most_common(k)]

        return result


        