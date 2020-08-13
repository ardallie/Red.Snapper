"""
 This module contains class Dataset
 to generate number of results using 4 processes
"""
import time
from multiprocessing import Process, Queue
from collections import OrderedDict
from redsnapper.modules.person import Person
from redsnapper.modules.gaussian import Gaussian
from redsnapper.modules.config import HEADERS


class Dataset:
    """ Generate a data set containing number of records specified in GUI """

    def run_workload(self, rows, **kw):
        """
        :param rows: total number of records to be generated
        :param kw: bundle of params passed from GUI, example below:
        {'pgender': 50, 'pdname': 25,
        'dob1': '1945', 'dob2': '1997', 'pdsurname': 15}
        :return: consolidated results from 4 processes
        """
        # Measure performance
        print("starting...")
        start = time.time()

        # Divide total rows by 4 (and avoid divide by zero error)
        qrt = int(rows * 0.25)
        # calculate remainder for 4th thread
        rem = int(rows - (qrt * 3))
        pk1 = 1
        pk2 = (qrt * 1) + 1
        pk3 = (qrt * 2) + 1
        pk4 = (qrt * 3) + 1

        # Process #1 - to compute 25% of workload
        qu1 = Queue()
        pr1 = Process(target=self.get_people, args=(qrt, pk1, qu1), kwargs=kw)
        pr1.start()
        # Process #2 - to compute 25% of workload
        qu2 = Queue()
        pr2 = Process(target=self.get_people, args=(qrt, pk2, qu2), kwargs=kw)
        pr2.start()
        # Process #3 - to compute 25% of workload
        qu3 = Queue()
        pr3 = Process(target=self.get_people, args=(qrt, pk3, qu3), kwargs=kw)
        pr3.start()
        # Process #4 - to compute 25% of workload (with small remainder)
        qu4 = Queue()
        pr4 = Process(target=self.get_people, args=(rem, pk4, qu4), kwargs=kw)
        pr4.start()
        # Queue management - get results back from function
        resp1 = qu1.get()
        pr1.join()
        resp2 = qu2.get()
        pr2.join()
        resp3 = qu3.get()
        pr3.join()
        resp4 = qu4.get()
        pr4.join()

        # Concatenate results from all processes in the Queue
        output = resp1 + resp2 + resp3 + resp4
        print("Number of records generated: " + str(len(output)))
        # measure performance
        end = time.time()
        print("Task completed in " + str(round(end - start, 1)) + " sec")
        return output

    @staticmethod
    def get_people(rows, pkey, queue, **kwargs):
        """
        generate birthdays that are distributed normally (Gaussian dist.)
        :param rows: number of records
        :param pkey: primary key
        :param queue: queue object
        :param kwargs: params from GUI, example below:
        {'pgender': 50, 'pdname': 25,
        'dob1': '1945', 'dob2': '1997', 'pdsurname': 15}
        :return: no return parameters
        """
        serie = []
        dob1 = "1/1/" + kwargs["dob1"]
        dob2 = "31/12/" + kwargs["dob2"]
        ratio = 0.1
        dob = Gaussian.randnormal_date(rows, dob1, dob2, ratio)
        for i in range(rows):
            current = Person.get_core_details(**kwargs)
            current["dob"] = dob[i]
            current["pk"] = pkey + i
            ordered = OrderedDict((n, current[n]) for n in HEADERS)
            serie.append(ordered)
        queue.put(serie)
        return
