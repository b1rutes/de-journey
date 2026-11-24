# Q1. Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        i = 0
        while i < len(nums) :
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    answer =[i , j]
                    break
                j = j+ 1    
            i= i+1          
        return answer
    
solution = Solution()
print(solution.twoSum([2,7,11,15], 10))