"""
An example person class for the demo video...

Created Summer, 2015

@author: kvlinden
"""

from datetime import date
import sys


class Person:
    """
    This class models a person.
    Invariants:
        first_name != ''
        gender in ['f', 'm', 'o']
        age > 0
    """

    VOTING_AGE = 18

    def __init__(self, first_name='Jane', last_name='Doe', gender='f',
                 birthdate=None):
        """ This constructs a new person object. """
        gender = gender.lower()
        if birthdate is None:
            birthdate = date.today()
        if self.is_valid_information(first_name, last_name, gender, birthdate):
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender
            self.birthdate = birthdate
        else:
            print('Invalid information: ' +
                  first_name + ',' + last_name + ',' + gender + ',' + str(birthdate))
            sys.exit(-1)

    def __str__(self):
        """ This formats a nice string for a person object. """
        if self.gender == 'f':
            honorific = 'Ms.'
        elif self.gender == 'm':
            honorific = 'Mr.'
        else:
            honorific = 'M.'
        return honorific + ' ' \
               + self.first_name + ' ' + self.last_name + ' ' \
               + self.gender + ' ' + str(self.birthdate)

    def is_valid_information(self, first_name, last_name, gender, birthdate):
        """Check the validity of the information based on the class invariant."""
        return first_name != '' \
               and gender in ['f', 'm', 'o'] \
               and birthdate <= date.today()

    def get_gender(self):
        """ This access the person's gender value. """
        return self.gender

    def get_fullname(self):
        """ This accesses the person's full name. """
        return self.first_name + ' ' + self.last_name

    def get_age(self):
        """ This computes and returns the person's age. """
        today = date.today()
        year_difference = today.year - self.birthdate.year
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            return year_difference - 1
        else:
            return year_difference

    def set_fullname(self, first_name, last_name):
        """ This changes the person's (full) name. """
        if self.is_valid_information(first_name, last_name, self.gender, self.birthdate):
            self.first_name = first_name
            self.last_name = last_name
        else:
            print('Invalid full name information: ' + first_name + ',' + last_name)
            sys.exit(-1)

    def is_voting_age(self):
        """ Determine if the person is of voting age. """
        return self.get_age() >= Person.VOTING_AGE

    def is_older_than(self, other_person):
        """ Determine if the person is older than other_person. """
        return self.get_age() > other_person.get_age()

ethan = Person.get_age()