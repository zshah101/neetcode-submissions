class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0 
        res = 0
        seen = {}
        while right < len(s):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
                
        
            while (right - left + 1) - (max(seen.values())) > k:
                seen[s[left]] -= 1
                left += 1
            
            freq = max(seen.values())
            length = right - left + 1
                
            res = max(res, length)
            right += 1
        return res







        