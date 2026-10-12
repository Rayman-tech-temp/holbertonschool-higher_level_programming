#!/usr/bin/env python3
import pickle
"""
this module is demostrating pickle.
"""


class CustomObject():

    """
    the class that has an inbuilt functions to
    make files and read files.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {0}\nAge: {1}\nIs Student: {2}".format(
                                                             self.name,
                                                             self.age,
                                                             self.is_student))

    def serialize(self, filename):
        """
        this writes the binary into a new file.
        """
        pickle_out = open(filename, "wb")
        pickle.dump(self, pickle_out)
        pickle_out.close()
        pass

    @classmethod
    def deserialize(cls, filename):
        """
        this opens a specified file with binary
        information and returns to the caller.
        """
        try:
            de_pickle = open(filename, "rb")
            output = pickle.load(de_pickle)
            return (output)

        except FileNotFoundError:
            return (None)
        except IOError:
            return (None)
