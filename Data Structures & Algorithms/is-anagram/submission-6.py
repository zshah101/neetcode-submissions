class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for word in s:
            if word in count_s:
                count_s[word] += 1
            else:
                count_s[word] = 1
        

        for word in t:
            if word in count_t:
                count_t[word] += 1
            else:
                count_t[word] = 1

        if count_s == count_t:
            return True
        else:
            return False 