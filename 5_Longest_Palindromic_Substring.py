"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

import unittest


class Solution:

    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = end = result = 0
        for i in range(len(s)):
            length1 = self.expand(s, i, i)
            length2 = self.expand(s, i, i + 1)
            result = max(length1, length2)
            if (end - start) < result:
                start = i - (result - 1) // 2
                end = i + (result // 2)
        return s[start:end + 1]


class UnitTest(unittest.TestCase):

    def test1(self):
        string = "abbba"
        res = Solution().longestPalindrome(string)
        answer = "abbba"
        self.assertEqual(res, answer)

    def test2(self):
        string = "abcdfgcdba"
        res = Solution().longestPalindrome(string)
        answer = "a"
        self.assertEqual(res, answer)

    def test3(self):
        string = "a"
        res = Solution().longestPalindrome(string)
        answer = "a"
        self.assertEqual(res, answer)

    def test4(self):
        string = ""
        res = Solution().longestPalindrome(string)
        answer = ""
        self.assertEqual(res, answer)

    def test5(self):
        string = "ahdaadls"
        res = Solution().longestPalindrome(string)
        answer = "daad"
        self.assertEqual(res, answer)


if __name__ == "__main__":
    unittest.main(verbosity=2)
