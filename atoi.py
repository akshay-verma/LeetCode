"""
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution(object):

    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        string = string.strip()
        result = 0
        minus = 1
        found = False
        for char in string:
            if char != ' ':
                try:
                    tmp = int(char)
                except ValueError as e:
                    if not found and char == "-":
                        found = True
                        minus = -1
                        continue
                    if not found and char == "+":
                        found = True
                        continue
                    break
                else:
                    found = True
                    result = result * 10 + int(char)
            else:
                break

        if result >= 2**31:
            if minus == -1:
                return minus * 2**31
            else:
                return 2**31 - 1
        return minus * result


print(Solution().myAtoi("2147483648"))
