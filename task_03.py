#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module simple for-loop to loop over a simple data construct."""


# Import Python libs
import decimal
import data

def lexicographics(to_analyze):
    """
    This function provides the maximum, minimum, and average length of words in
    a speech performing a lexicographical analysis not unlike what's used to
    measure reading level.

    Args:
        to_analyze (str): string to find max min, and avg.

    Returns:
        mixed: 

    Examples:

        

    """
    words = (to_analyze.split('\n'))
    maxnum = 0
    minnum = 0
    avgnum = 0
    for items in words:
        maxnum = max(items.split())
        
        return len(max(maxnum))
