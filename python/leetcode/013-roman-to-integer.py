# Q13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = []
        digit = 0
        i = 0
        romans = {'I':1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }

        numbers =[romans[char] for char in s]
   
        while i < len(numbers):
            if i == len(numbers)-1:
                digit = digit + numbers[i] 
            elif numbers[i] < numbers[i+1]:
                digit = digit + (numbers[i+1] - numbers[i])
                i = i + 2
                continue
            else:
                digit = digit + numbers[i]    
            
            i = i+1
            
        return (digit)         
    

solution = Solution()
print(solution.romanToInt("III"))