class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #bat - #abt, tba, bta
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word)) # tca - a, c, t - act

            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        # { act: [tca, atc, cat], pots: [tops, sopt, opts]}
        return list(hashmap.values())        
        