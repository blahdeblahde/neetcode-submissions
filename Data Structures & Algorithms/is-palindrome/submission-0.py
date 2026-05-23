class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(c for c in s if c.isalnum())
        
        return(result.lower() == result[::-1].lower())