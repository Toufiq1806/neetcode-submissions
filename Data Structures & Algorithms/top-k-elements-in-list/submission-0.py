from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        freq=dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        ret=[]
        for i in freq.keys():
            if len(ret)<k:
                ret.append(i)
        return ret

        
            
