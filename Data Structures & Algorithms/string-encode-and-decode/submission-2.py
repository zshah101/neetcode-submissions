class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = str(len(word))
            string += length + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = length + start
            word = s[start:end]
            i = end
            res.append(word)
        return res
            
            
