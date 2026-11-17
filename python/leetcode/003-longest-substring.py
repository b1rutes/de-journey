# Q3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_list = []
        long_substring = ""
        max_len = 0
        for char in s:
            while char in substring_list:
                substring_list.pop(0)
            substring_list.append(char)
            
            if max_len < len(substring_list):
                max_len = len(substring_list)
                long_substring = "".join(substring_list)
    
        return len(long_substring)

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))   