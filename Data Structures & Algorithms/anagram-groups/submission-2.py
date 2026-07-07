class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group = []
        # visited = set()

        # for i in range(len(strs)): #O(n)
        #     if i in visited:
        #         continue
            
        #     current_group = [strs[i]]
        #     visited.add(i)

        #     for j in range(i+1, len(strs)): #O(n)
        #         if sorted(strs[i]) == sorted(strs[j]): #O(N log N)
        #             current_group.append(strs[j])
        #             visited.add(j)

        #     group.append(current_group)
        # return group #On^2(nlogn)

        #cat: act, tac, cta

        group = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) #atc -> a,c,t -> act

            if sorted_word in group:
                group[sorted_word].append(word)
            else:
                group[sorted_word] = [word]
        return list(group.values())


