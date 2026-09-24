class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        l = 0 
        r = 0
        res = 0
        seen = {}
        while r < len(s):
            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            
            while (r - l + 1) - (max(seen.values())) > k:
                seen[s[l]] -= 1
                l += 1
            length = r - l + 1

            res = max(res, length)
            r += 1
        return res 
                          

             

            
            


