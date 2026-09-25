class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
        # for i in range(len(s)):
        #     seen = {} # {A : 2, B : 1}
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             seen[s[j]] += 1
        #         else:
        #             seen[s[j]] = 1
        #         length = j - i + 1
        #         if (length - max(seen.values())) <= k:
        #             res = max(res, length)    
        # return res 

        # A A B B C D

        i = 0
        res = 0 
        j = 0
        seen = {}
        while j < len(s):
            if s[j] in seen:
                seen[s[j]] += 1
            else:
                seen[s[j]] = 1

            while ((j - i + 1) - max(seen.values())) > k:
                seen[s[i]] -= 1
                i += 1
                
            length = j - i + 1
            
            res = max(res, length)
            j += 1

                
        return res             

            

                

        