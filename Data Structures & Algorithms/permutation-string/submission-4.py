class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #s1 = abc
        #s2 = shabc-ee
        # a - 97#
        # b - a = 98 - 97 = 1
        #[1,1,1,0,0,0,1,1,1]
        if len(s1) > len(s2):
            return False 
            
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        #count1 = [1, 1, 1, 0 , 0 , 0]
        #count2 = [1, 0, 0, 0, 1, 1, 1]
        if count1 == count2:
            return True 

        k = len(s1)
        # lecabee
        for i in range(k, len(s2)):
            count2[ord(s2[i]) - ord("a")] += 1
            count2[ord(s2[i - k]) - ord("a")] -= 1

            if count1 == count2:
                return True
        return False 