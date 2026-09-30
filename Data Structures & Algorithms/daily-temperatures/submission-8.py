class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #30(0), 
    
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                curr = stack.pop()
                days = i - curr
                res[curr] = days
            stack.append(i)
        return res 
        