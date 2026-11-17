# Q9. Palindrome Number - https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        num = x
        rem = 0
        digit = 0
        
        while num != 0:
            rem  = num % 10
            digit = (digit * 10) + rem
            num = num // 10 

        return x == digit
          

solution = Solution()
print(solution.isPalindrome(121))