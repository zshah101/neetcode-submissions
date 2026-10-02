class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # XYYX
        i = 0
        j = 0
        res = 0
        seen = {}

        while j < len(s):
            if s[j] in seen:
                seen[s[j]] += 1
            else:
                seen[s[j]] = 1
            
            while (j - i + 1) - (max(seen.values())) > k:
                seen[s[i]] -= 1
                i += 1
            res =  max(res, (j - i + 1))

            j += 1
        return res 
            
                                