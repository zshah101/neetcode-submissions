class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        if clean == clean[::-1]:
            return True
        else:
            return False 
        
        
