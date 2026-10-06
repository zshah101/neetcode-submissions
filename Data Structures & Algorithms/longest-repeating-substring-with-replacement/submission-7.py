class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #APPLE
        left = 0
        res = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            
            while (right - left + 1) - (max(seen.values())) > k:
                seen[s[left]] -= 1
                left += 1
            res = max(res, (right - left + 1))
        return res 
        