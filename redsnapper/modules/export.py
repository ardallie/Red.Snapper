"""
 This module contains class Export
 to handle the exporting data to JSON and CSV formats
"""
import csv
import json
from tkinter import filedialog, messagebox
from redsnapper.modules.config import HEADERS


class Export:
    """ Exports data to JSON or CSV """

    @staticmethod
    def info_error():
        """
        Show error message if file could not be saved
        :return: no return parameters
        """
        message = 'File could not be saved.'
        messagebox.showinfo(title="File not saved", message=message)
        return

    @staticmethod
    def info_success(save_as):
        """
        Show success message if file was saved correctly
        :return: no return parameters
        """
        message = 'File was saved successfully as ' + save_as
        messagebox.showinfo(title="File saved.", message=message)
        return

    def to_json(self, dataset):
        """
        Exports data to JSON
        :param dataset: dict with generated data
        :return: no return parameters
        """
        save_as = filedialog.asksaveasfilename(defaultextension='.json')
        try:
            with open(save_as, 'w', newline='') as file:
                json.dump(dataset, file)
            self.info_success(save_as)
        except IOError:
            self.info_error()
        return

    def to_csv(self, dataset):
        """
        Exports data to CSV
        :param dataset: dict with generated data
        :return: no return parameters
        """
        save_as = filedialog.asksaveasfilename(defaultextension='.csv')
        try:
            with open(save_as, 'w', newline='') as file:
                scribe = csv.writer(file)
                scribe.writerow(HEADERS)
                for row in dataset:
                    scribe.writerow(row.values())
            self.info_success(save_as)
        except IOError:
            self.info_error()
        return
