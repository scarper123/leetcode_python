#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 15:44
# @Author  : Shanming Liu

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

"""
from utils import time_record


class Solution(object):
    @time_record
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_l = len(s)
        if s_l <= 1:
            return s
        elif s_l == 2:
            if check_is_palindrome(s):
                return s
            return s[0]

        def parse_string():
            for inx in range(s_l):
                tmp = s[inx]
                start = inx + 1
                while start < s_l:
                    tmp = "%s%s" % (tmp, s[start])

                    if check_is_palindrome(tmp):
                        yield tmp

                    start += 1

        max_value = ""
        for item in parse_string():
            if len(item) > len(max_value):
                max_value = item

        return max_value


def check_is_palindrome(s):
    mid = len(s) / 2
    if len(s) % 2 > 0:
        left = s[:mid]
        right = s[mid + 1:]
    else:
        left = s[:mid]
        right = s[mid:]

    return all(vl == right[mid - 1 - inx] for inx, vl in enumerate(left))


if __name__ == '__main__':
    # assert check_is_palindrome("bababab")

    tmp = "iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx"
    s = Solution()
    print(s.longestPalindrome(tmp))
    # assert s.longestPalindrome("babad") == "bab"
    # assert s.longestPalindrome("cbbd") == "bb"
