class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group = []
        # visited = set()

        # for i in range(len(strs)):
        #     if i in visited:
        #         continue
            
        #     current_group = [strs[i]]
        #     visited.add(i)
            
        #     for j in range(i+1, len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             current_group.append(strs[j])
        #             visited.add(j)
        #     group.append(current_group)
            
        # return group   

        group = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in group:
                group[sorted_word].append(word)
            else:
                group[sorted_word] = [word]

        return list(group.values())

