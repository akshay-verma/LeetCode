"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for index, numeral in enumerate(s):
            total += symbol[numeral]
            if numeral == "V" or numeral == "X":
                if index > 0 and s[index - 1] == "I":
                    total -= 2 * symbol[s[index - 1]]
            elif numeral == "L" or numeral == "C":
                if index > 0 and s[index - 1] == "X":
                    total -= 2 * symbol[s[index - 1]]
            elif numeral == "D" or numeral == "M":
                if index > 0 and s[index - 1] == "C":
                    total -= 2 * symbol[s[index - 1]]
        return total


print(Solution().romanToInt("CCXLVI"))
