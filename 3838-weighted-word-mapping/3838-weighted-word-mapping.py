class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for i in words:
            s=0
            for j in i:
                s+=(weights[ord(j)-ord("a")])
            s=s%26
            ans=ans+chr(ord("z")-s)
        
        return ans