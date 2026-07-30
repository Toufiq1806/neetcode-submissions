from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=dict(sorted(Counter(nums).items(),key=lambda x:x[1],reverse=True))
        return list(a)[0]
        