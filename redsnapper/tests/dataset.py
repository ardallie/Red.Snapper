"""
 This module contains unit tests for class Dataset
"""
import unittest
from multiprocessing import Process, Queue
from redsnapper.modules.utils import get_rand
from redsnapper.modules.dataset import Dataset
from redsnapper.tests.test_config import KWG


class TestDataset(unittest.TestCase):
    """
    Class containing all Dataset unit tests.
    """

    @staticmethod
    def test_queue():
        """
        :return: true if test passed, false if not
        """
        print("Generates dataset using Queue.")
        dset = Dataset()
        queue = Queue()
        rows = get_rand(100, 200)
        pkey = get_rand(10, 1000)
        # Start process and push to queue
        proc = Process(target=dset.get_people, args=(rows, pkey, queue),
                       kwargs=KWG)
        proc.start()

        # Queue management - get results back from function
        response = queue.get()
        proc.join()
        reslen = len(response)
        # Test if generated output has a correct number of items
        assert reslen == rows
        # Test if first item has a correct primary key number
        assert response[0]["pk"] == pkey
        # Test if second item has a correct primary key number
        assert response[1]["pk"] == pkey + 1
        # Test if third item has a correct primary key number
        assert response[2]["pk"] == pkey + 2

    @staticmethod
    def test_run_workload():
        """
        :return: true if test passed, false if not
        """
        print("Generates dataset using Queue and 4 processes")
        dset = Dataset()
        rows = get_rand(100, 200)
        response = dset.run_workload(rows, **KWG)
        reslen = len(response)
        # Test if generated output has a correct number of items
        assert reslen == rows


if __name__ == '__main__':
    unittest.main()
