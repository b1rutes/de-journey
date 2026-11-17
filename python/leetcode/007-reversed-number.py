# Q7 Reversed Number - https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        num = x
        rem = 0
        digit = 0

        if num < 0:
            num *= -1
        
        while num != 0:
            rem  = num % 10
            digit = (digit * 10) + rem
            num = num // 10 

        if x < 0:
            digit *= -1 

        if -2147483648 <= digit <= 2147483647:
            return digit 
        else:
            return 0          

solution = Solution()
print(solution.reverse(123))
