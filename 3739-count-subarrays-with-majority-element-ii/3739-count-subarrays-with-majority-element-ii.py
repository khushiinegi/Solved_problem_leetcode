class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 2
        size = 2 * n + 5
        
        bit = [0] * size
        
        def add(i, val):
            while i < size:
                bit[i] += val
                i += i & -i
        
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        
        ans = 0
        prefix = 0
        
        add(offset, 1)   # prefix sum 0
        
        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1
            
            # need previous prefix < current prefix
            ans += query(prefix + offset - 1)
            
            add(prefix + offset, 1)
        
        return ans
        