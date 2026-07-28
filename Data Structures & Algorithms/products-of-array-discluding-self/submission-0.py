class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        put=1
        for i,n in enumerate(nums):
            if i > 0:
                extra=nums[:i] 
                for k in extra:
                    put*=k
            for j in range(i+1,len(nums)):
                put*=nums[j]
            output.append(put)   
            put=1
        return output