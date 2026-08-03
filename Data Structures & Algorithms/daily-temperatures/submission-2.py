class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #[0,0,0,0,0]
        stack = [] #[0, ]

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop() #0 
                res[prev] = i - prev 
            stack.append(i)
        return res

        