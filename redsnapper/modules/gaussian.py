"""
 This module contains class Gaussian
 to generate data column of normally distributed birthdays
"""
import numpy as np
import arrow
from redsnapper.modules.utils import flip_timestamp


class Gaussian:
    """ Generate a data set containing normally distributed birthdays """

    @staticmethod
    def randnormal_int(loc, scale, size=100):
        """
        Generates serie of normally distributed numbers
        :param loc: centre of the distribution
        :param scale: standard dev.
        :param size: number of records
        :return:
        """
        dist = np.random.normal(loc, scale, size)
        return dist.tolist()

    @staticmethod
    def randnormal_date(size, start, end, ratio):
        """
        :param size: number of records
        :param start: earliest birthday
        :param end: latest birthday
        :param ratio: could be roughly compared to standard deviation
        """
        date_range = start, end
        prepme_rng = tuple(arrow.get(d, "D/M/YYYY") for d in date_range)
        tstamp_range = tuple(d.timestamp for d in prepme_rng)
        loc = (tstamp_range[0] + tstamp_range[1]) * 0.5
        scale = (tstamp_range[1] - tstamp_range[0]) * ratio
        dist = np.random.normal(loc, scale, size)
        output = []
        for item in np.sort(dist):
            entry = flip_timestamp(item)
            entry = arrow.get(entry).format("DD/MM/YYYY")
            output.append(entry)
        return output
