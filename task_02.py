#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module runs an if, else statement."""


def bool_to_str(bval):
    """
    This function can return a 'yes' or 'no'value equivalent of truthy
    or falsy values.

    Args:
        bval (mixed): value for the if statement

    Returns:
        str: Yes or No

    Examples:

        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'

        >>> import task_02
        >>> task 02.bool_to_str('')
        'No'

    """
    answer = 0
    if bval:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer
