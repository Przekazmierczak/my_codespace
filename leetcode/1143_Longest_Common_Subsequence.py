"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def longestCommonSubsequence(self, text1, text2):
        LEN1 = len(text1)
        LEN2 = len(text2)

        dp = [[0 for _ in range(LEN1 + 1)] for _ in range(LEN2 + 1)]
        
        for i in range(1, LEN2 + 1):
            for j in range(1, LEN1 + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (text1[j - 1] == text2[i - 1]))
        
        return dp[-1][-1]
    
def main():
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"

    solution = Solution()

    result = solution.longestCommonSubsequence(text1, text2)
    
    print(result)


if __name__ == "__main__":
    main()