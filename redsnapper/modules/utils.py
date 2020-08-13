"""
    This module contains utility functions
"""
import random
import datetime as dt
from datetime import datetime


def roll():
    """
    Returns a random number between 1 and 100
    :return: integer containing random number between 1 and 100
    """
    return random.randint(1, 100)


def get_rand(lower, upper):
    """
    Returns a random number in range
    :param lower: range bottom
    :param upper: range top
    :return: Returns a random number in range
    """
    return random.randint(lower, upper)


def flip_timestamp(timestamp):
    """
    Converts dates from a negative timestamp (older than 1 Jan 1970)
    :param timestamp: timestamp
    :return: correct date
    """
    if int(timestamp) < 0:
        flip = dt.datetime(1970, 1, 1) + dt.timedelta(seconds=timestamp)
    else:
        flip = datetime.fromtimestamp(timestamp)
    return flip
