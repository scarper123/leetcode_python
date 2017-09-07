#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-06 22:05:36
# @Author  : Shanming (18021540285@163.com)
# @Link    : http://example.org
# @Version : $Id$

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1 = evaluate_value(l1)
        v2 = evaluate_value(l2)
        return dispose_value(v1 + v2)


def evaluate_value(data):
    res = 0
    for inx, item in enumerate(iter_node(data)):
        res += item * pow(10, inx)
    return res


def dispose_value(value):
    print(value)
    res = [ListNode(int(i)) for i in str(value)]
    node = next_node = res[-1]

    if len(res) <= 1:
        return node

    index = len(res) - 1
    while index >= 0:
        tmp_node = res[index]
        next_node.next = tmp_node
        next_node = tmp_node
        index -= 1

    return node


def iter_node(l):
    yield l.val
    next_node = l.next
    while next_node:
        yield next_node.val
        next_node = next_node.next


if __name__ == '__main__':
    # print(evaluate_value([2, 4, 3]))
    s = Solution()
    # l1 = [ListNode(i) for i in [2, 4, 3]]
    # l2 = [ListNode(i) for i in [5, 6, 4]]
    # print(s.addTwoNumbers(l1, l2))
    node1 = ListNode(0)
    # node2 = ListNode(4)
    # node3 = ListNode(3)
    # node1.next = node2
    # node2.next = node3

    node4 = ListNode(0)
    # node5 = ListNode(6)
    # node6 = ListNode(4)
    # node4.next = node5
    # node5.next = node6

    for i in iter_node(s.addTwoNumbers(node1, node4)):
        print i
