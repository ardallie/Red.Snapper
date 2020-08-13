"""
    This module contains class Person generating random data
    using predefined choices from folder 'data'
"""

import string
import random
from redsnapper.modules.utils import roll, get_rand
from redsnapper.data.names_male import names_male
from redsnapper.data.names_female import names_female
from redsnapper.data.surnames import surnames
from redsnapper.data.streets import streets
from redsnapper.data.towns import towns
from redsnapper.data.emails import emails
from redsnapper.data.jobs import jobs


class Person:
    """ Contains functions generating data for a single 'person' """

    @staticmethod
    def get_full_name(pgender=50, pdname=50, pdsurname=50, **kwargs):
        """
        Generates the full name for a single person.
        :param pgender: probability % of getting a female gender
        :param pdname: probability % of getting a double name
        :param pdsurname: probability % of getting a double surname
        :param kwargs: parameters from GUI, example below:
        {'pgender': 50, 'pdname': 25,
        'dob1': '1945', 'dob2': '1997', 'pdsurname': 15}
        :return: the dict containing first names, last names and gender
        """
        gender = "f" if roll() <= pgender else "m"
        double_name = True if roll() <= pdname else False
        double_surname = True if roll() <= pdsurname else False
        names = names_male if gender == "m" else names_female

        name1 = random.choice(names)
        name2 = ""
        if double_name:
            name2 = random.choice(names)
            while name1 == name2:
                name2 = random.choice(names)

        surname1 = random.choice(surnames)
        surname2 = ""
        if double_surname:
            surname2 = random.choice(surnames)
            while surname1 == surname2:
                surname2 = random.choice(surnames)

        dupex = surname1 == name1 or (surname2 == name1 and name1 != "")
        dupey = surname1 == name2 or (surname2 == name2 and name2 != "")
        dupe = dupex is True or dupey is True

        # Recursive function - a base case
        # name is different that surname
        if dupe is False:
            if surname2 == "":
                surname = surname1
            else:
                surname = surname1 + " - " + surname2

            if name2 == "":
                forenames = name1
            else:
                forenames = name1 + " " + name2

            full_name = forenames + " " + surname
            full_name = {
                "first_name": name1,
                "middle_name": name2,
                "surname": surname,
                "surname1": surname1,
                "surname2": surname2,
                "full_name": full_name,
                "sex": gender
            }
            return full_name
        else:
            # Recursive function call
            # re-do if first, middle names or surnames are identical
            # simpler and more elegant approach compared to ifs and whiles
            return Person.get_full_name(pgender, pdname, pdsurname, **kwargs)

    @staticmethod
    def get_street():
        """
        Street
        :return: house number and street name
        """
        par1 = random.randint(1, 150)
        par2 = random.choice(streets)
        street = "{0} {1}".format(par1, par2)
        return street

    @staticmethod
    def get_town():
        """
        Town name
        :return: random town name
        """
        return random.choice(towns)

    @staticmethod
    def get_postcode(prefix):
        """
        postcode, first part belongs to the town and second part is random
        :param prefix: first part of postcode (eg. W12)
        :return: full postcode (eg. W12 3AA)
        """
        letters = string.ascii_uppercase
        full_postcode = "{0} {1}{2}{3}".format(prefix,
                                               random.randint(1, 9),
                                               random.choice(letters),
                                               random.choice(letters))
        return full_postcode

    @staticmethod
    def get_full_address():
        """
        Combine street, town, postcode into full address
        :return: dict containing a full address
        """
        _town = Person.get_town()
        full_address = {
            "street": Person.get_street(),
            "postcode": Person.get_postcode(_town["p"]),
            "town": _town["t"],
            "county": _town["c"]
        }
        return full_address

    @staticmethod
    def get_nin():
        """
        Generates the national insurance number
        returns the string that is 9 character long and complies with
        [LL][IIIIII][L] format (L = letter, I = integer)
        :return: string containing a random NIN
        """
        letters = string.ascii_uppercase
        par1 = "{0}{1}".format(random.choice(letters), random.choice(letters))
        par2 = random.randint(100000, 999999)
        par3 = random.choice(letters)
        nin = "{0}{1}{2}".format(par1, par2, par3)
        return nin

    @staticmethod
    def get_mobile():
        """
        Generates the mobile phone number
        :return: string containing a random mobile phone number
        """
        return "0" + str(random.randint(7101234567, 7998765432))

    @staticmethod
    def get_email(per, choice):
        """
        Generates the email address
        :param per: dict with already generated data (name, surname etc.)
        :param choice: random number to determine format of email
        :return: string with email based on name / surname
        """
        # Emulating switch statement in Python
        # http://blog.simonwillison.net/post/57956755106/switch
        username = {
            "0": lambda x: per["surname1"],
            "1": lambda x: per["first_name"] + per["surname1"],
            "2": lambda x: per["first_name"] + "_" + per["surname1"],
            "3": lambda x: per["first_name"][0] + per["surname1"],
            "4": lambda x: per["first_name"][0] + "_" + per["surname1"],
            "5": lambda x: per["first_name"] + per["surname1"][0],
            "6": lambda x: per["surname1"] + per["first_name"],
            "7": lambda x: per["first_name"] + str(roll()),
            "8": lambda x: per["surname1"] + str(roll()),
            "9": lambda x: per["first_name"][0] + per["surname1"] + str(roll())
        }[choice](True)
        domain = random.choice(emails)
        email = username.lower() + "@" + domain
        return email

    @staticmethod
    def get_job_title():
        """
        Generates the job title
        :return: string with randomly selected job title
        """
        return random.choice(jobs)

    @staticmethod
    def get_core_details(**kwargs):
        """
        Generates one row with core details:
        full name, address, mobile, nin

        :param kwargs: parameters from GUI, example below:
        {'pgender': 50, 'pdname': 25,
        'dob1': '1945', 'dob2': '1997', 'pdsurname': 15}
        :return: dict with generated details
        """
        entry = {}
        # Returns two dicts
        person = Person.get_full_name(**kwargs)
        address = Person.get_full_address()
        # Since data type for address is dict, it needs to be flattened first
        row = dict(person, **address)
        entry.update(row)
        # Get additional data and add as pairs of keys & values
        choice = str(get_rand(0, 9))
        email = Person.get_email(person, choice)
        entry["email"] = email
        entry["nin"] = Person.get_nin()
        entry["mobile"] = Person.get_mobile()
        entry["job_title"] = Person.get_job_title()
        entry["salary"] = get_rand(18000, 90000)
        return entry
