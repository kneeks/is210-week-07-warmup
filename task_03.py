#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module simple for-loop to loop over a simple data construct."""


# Import Python libs
import decimal


def lexicographics(to_analyze):
    """
    This function provides the maximum, minimum, and average length of words in
    a speech performing a lexicographical analysis not unlike what's used to
    measure reading level.

    Args:
        to_analyze (str): string to find max min, and avg.

    Returns:
        mixed: max, min, avg

    Examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))

    """
    words = (to_analyze.split('\n'))
    list1 = []
    for items in words:
        nums = len(items.split())
        list1.append(nums)
    return max(list1), min(list1), (sum(list1) / decimal.Decimal(len(list1)))
