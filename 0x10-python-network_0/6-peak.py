#!/usr/bin/python3
"""Finds the peak in an unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds the peak in an unsorted list of ints"""
    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return _find_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]
