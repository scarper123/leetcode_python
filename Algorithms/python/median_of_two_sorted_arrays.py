#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-07 10:12
# @Author  : Shanming Liu

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = nums1 + nums2
        nums.sort()
        ood = True if len(nums) % 2 > 0 else False
        mid = len(nums) / 2
        if ood:
            return nums[mid]
        return (nums[mid - 1] + nums[mid]) / 2.0


if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
