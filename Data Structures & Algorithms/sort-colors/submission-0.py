class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for i in nums:
            if i == 0:
                count[0]+=1
            elif i ==1:
                count[1]+=1
            elif i==2:
                count[2]+=1
            index=0
            for i in range(3):
                for j in range(count[i]):
                    nums[index]=i
                    index+=1
                
        
            



        