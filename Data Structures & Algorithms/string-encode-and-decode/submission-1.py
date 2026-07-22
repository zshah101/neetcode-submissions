class Solution:
    def encode(self, strs):
        #["Hello", "World"]
        res = ""
        for word in strs:
            length = str(len(word))
            res += length + "!" + word
        # res = "5#Hello5#World"
        return res
    
    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1
            
            length = int(s[i:j])
            word_start = j + 1
            word_end = length + word_start
            word = s[word_start:word_end]

            res.append(word)
            i = word_end
        return res