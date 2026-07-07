class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        visited = set()

        for i in range(len(strs)): #O(n)
            if i in visited:
                continue
            
            current_group = [strs[i]]
            visited.add(i)

            for j in range(i+1, len(strs)): #O(n)
                if sorted(strs[i]) == sorted(strs[j]): #O(N log N)
                    current_group.append(strs[j])
                    visited.add(j)

            group.append(current_group)
        return group #On^2(nlogn)


