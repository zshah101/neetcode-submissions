class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            steps = 0
            for j in range(i+1, len(temperatures)):
                steps += 1
                if temperatures[j] > temperatures[i]:
                    res.append(steps)
                    break
            else:
                res.append(0)
        return res