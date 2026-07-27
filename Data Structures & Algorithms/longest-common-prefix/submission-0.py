class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=[]
        if not strs:
            return ""
        for i in zip(*strs):
            if (len(set(i))==1):
                out.append(i[0])
            else:
                break
        return "".join(out)

       



            
           

            