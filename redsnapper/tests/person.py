"""
 this module contains unit tests for class Person
"""
import unittest
from redsnapper.modules.person import Person
from redsnapper.data.surnames import surnames
from redsnapper.data.names_male import names_male
from redsnapper.data.names_female import names_female
from redsnapper.tests.test_config import ITLG


class TestPerson(unittest.TestCase):
    """
    class containing all Person unit tests.
    each assertion is iterated X times (modify constant ITR)
    """

    @staticmethod
    def test_name_non_empty():
        """
        :return: true if test passed, false if not
        """
        print("First and middle names are not empty. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(50, 100, 50)
            name1 = len(full_name.get("first_name"))
            name2 = len(full_name.get("middle_name"))
            assert name1 > 0 and name2 > 0

    @staticmethod
    def test_surname_non_empty():
        """
        :return: true if test passed, false if not
        """
        print("Last names are not empty. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(50, 50, 100)
            surname1 = len(full_name.get("surname1"))
            surname2 = len(full_name.get("surname2"))
            assert surname1 > 0 and surname2 > 0

    @staticmethod
    def test_double_name():
        """
        :return: true if test passed, false if not
        """
        print("Inequality of first and middle names. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(100, 100, 0)
            name1 = full_name.get("first_name")
            name2 = full_name.get("middle_name")
            assert name1 != name2

    @staticmethod
    def test_double_surname():
        """
        :return: true if test passed, false if not
        """
        print("Inequality in surnames. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(50, 0, 100)
            surname1 = full_name.get("surname1")
            surname2 = full_name.get("surname2")
            assert surname1 != surname2

    @staticmethod
    def test_male_name():
        """
        :return: true if test passed, false if not
        """
        print("Male names are from correct list. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(0, 100, 0)
            name1 = full_name.get("first_name")
            name2 = full_name.get("middle_name")
            assert name1 in names_male and name2 in names_male

    @staticmethod
    def test_female_name():
        """
        :return: true if test passed, false if not
        """
        print("Female names are from correct list. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(100, 100, 0)
            name1 = full_name.get("first_name")
            name2 = full_name.get("middle_name")
            assert name1 in names_female and name2 in names_female

    @staticmethod
    def test_surname():
        """
        :return: true if test passed, false if not
        """
        print("Surnames are from correct list. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(50, 50, 100)
            surname1 = full_name.get("surname1")
            surname2 = full_name.get("surname2")
            assert surname1 in surnames and surname2 in surnames

    @staticmethod
    def test_name_neq_surname():
        """
        :return: true if test passed, false if not
        """
        print("Surname is different than names. Loop:", ITLG)
        for _i in range(ITLG):
            full_name = Person.get_full_name(50, 40, 40)
            name1 = full_name.get("first_name")
            name2 = full_name.get("middle_name")
            surname1 = full_name.get("surname1")
            surname2 = full_name.get("surname2")
            if surname2 == "" and name2 == "":
                assert name1 != surname1, full_name
                assert name2 != surname1, full_name
            else:
                assert name1 != surname1 and name1 != surname2, full_name
                assert name2 != surname1 and name2 != surname2, full_name

    @staticmethod
    def test_street_format():
        """
        :return: true if test passed, false if not
        """
        print("Street starts with number, ends with letter. Loop:", ITLG)
        for _i in range(ITLG):
            value = Person.get_street()
            left = value[:1].isnumeric()
            right = value[-1:].isnumeric()
            assert left is True and right is False

    @staticmethod
    def test_postcode_format():
        """
        :return: true if test passed, false if not
        """
        print("Postcode complies with the format. Loop:", ITLG)
        for _i in range(ITLG):
            town = Person.get_town()
            value = Person.get_postcode(town["p"])
            left = value[:1].isnumeric()
            mid = value[-3:-2].isnumeric()
            right = value[-1:].isnumeric()
            assert left is False and mid is True and right is False

    @staticmethod
    def test_town_non_empty():
        """
        :return: true if test passed, false if not
        """
        print("Town is not empty. Loop:", ITLG)
        for _i in range(ITLG):
            value = len(Person.get_town())
            assert value > 0

    @staticmethod
    def test_full_address_non_empty():
        """
        :return: true if test passed, false if not
        """
        print("Full address doesn't contain empty values. Loop:", ITLG)
        for _i in range(ITLG):
            value = Person.get_full_address()
            valen = len(value)
            part1 = len(value["street"]) > 0 and len(value["postcode"]) > 0
            part2 = len(value["town"]) > 0 and len(value["county"]) > 0
            assert valen > 0
            assert part1
            assert part2

    @staticmethod
    def test_nin_format():
        """
        :return: true if test passed, false if not
        """
        print("NIN complies with the [LL][IIIIII][L] format. Loop:", ITLG)
        for _i in range(ITLG):
            value = Person.get_nin()
            valen = len(value)
            left = value[:1].isnumeric()
            mid = value[-7:-1].isnumeric()
            right = value[-1:].isnumeric()
            assert valen == 9 and left is False
            assert mid is True and right is False

    @staticmethod
    def test_email_0():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 0", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '0')
            user = email.index('@')
            cmp = person["surname1"].lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_1():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 1", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '1')
            user = email.index('@')
            cmp = (person["first_name"] + person["surname1"]).lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_2():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 2", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '2')
            user = email.index('@')
            cmp = (person["first_name"] + "_" + person["surname1"]).lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_3():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 3", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '3')
            user = email.index('@')
            cmp = (person["first_name"][0] + person["surname1"]).lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_4():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 4", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '4')
            user = email.index('@')
            cmp = (person["first_name"][0] + "_" + person["surname1"]).lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_5():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 5", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '5')
            user = email.index('@')
            cmp = (person["first_name"] + person["surname1"][0]).lower()
            assert email[:user] == cmp

    @staticmethod
    def test_email_6():
        """
        :return: true if test passed, false if not
        """
        print("Email address has correct format - type 6", ITLG)
        for _i in range(ITLG):
            person = Person.get_core_details()
            email = Person.get_email(person, '6')
            user = email.index('@')
            cmp = (person["surname1"] + person["first_name"]).lower()
            assert email[:user] == cmp


if __name__ == '__main__':
    unittest.main()
