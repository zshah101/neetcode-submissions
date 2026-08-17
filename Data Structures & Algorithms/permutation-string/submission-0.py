class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1) # 3
        len2 = len(s2)
        if len1 > len2:
            return False
        
        c1 = [0] * 26
        c2 = [0] * 26
         #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        for i in range(len1):
            c1[ord(s1[i]) - ord("a")] += 1
            c2[ord(s2[i]) - ord("a")] += 1

        if c1 == c2:
            return True
        
        for i in range(len1, len2):
            c2[ord(s2[i]) - ord("a")] += 1

            c2[ord(s2[i - len1]) - ord("a")] -= 1

            if c1 == c2:
                return True
        return False        


                
        
        