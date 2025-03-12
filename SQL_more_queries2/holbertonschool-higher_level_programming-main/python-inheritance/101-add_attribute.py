#!/usr/bin/python3
"""This module contains add_attribute() function"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object.

    Parameters
    ----------
        obj : object
        name : str
        value : any
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
