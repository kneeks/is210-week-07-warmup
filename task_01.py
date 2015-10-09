#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module runs a while loop."""


def fibonacci(maxint):
    """
    This is a Fibonacci sequence generator function with a while loop.

    Args:
        maxint (int): sets the mac interger for the while loop

    Returns:
        int: list of integers appended from the while loop

    Examples:

        >>> import task_01
        >>> task_01.fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

    """
    list1 = [0, ]
    lastnum, curnum = 0, 1
    while curnum < maxint:
        list1.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return list1
