"""
 this module contains unit tests for class Gaussian
"""
import unittest
import arrow
from redsnapper.modules.gaussian import Gaussian
from redsnapper.modules.utils import get_rand
from redsnapper.tests.rand_dates import date_ranges
from redsnapper.tests.test_config import ITSM


class TestGaussian(unittest.TestCase):
    """
    class containing all Gaussian unit tests.
    each assertion is iterated X times (modify constant ITSM)
    """

    @staticmethod
    def test_dates_length():
        """
        :return: true if test passed, false if not
        """
        print("Generates correct number of dates. Loop:", ITSM)
        for _i in range(ITSM):
            records = get_rand(10, 100)
            dobs = '1/12/1961'
            dobe = '01/01/1985'
            ratio = 0.15
            dob = len(Gaussian.randnormal_date(records, dobs, dobe, ratio))
            assert dob == records

    @staticmethod
    def test_dates_range():
        """
        :return: true if test passed, false if not
        """
        print("Generates dates within the given range. Loop:", ITSM)
        for _i in date_ranges:
            records = get_rand(10, 100)
            ratio = 0.09
            _lo = _i[0]
            _hi = _i[1]
            sample = Gaussian.randnormal_date(records, _lo, _hi, ratio)
            lots = (arrow.get(_lo, 'D/M/YYYY')).timestamp
            hits = (arrow.get(_hi, 'D/M/YYYY')).timestamp
            for item in sample:
                nts = (arrow.get(item, 'D/M/YYYY')).timestamp
                assert lots <= nts <= hits


if __name__ == '__main__':
    unittest.main()
