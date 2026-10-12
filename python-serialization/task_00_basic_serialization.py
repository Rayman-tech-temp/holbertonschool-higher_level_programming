#!/usr/bin/env python3

import pickle
"""
this is the pickle factory herer we pickle the info
into a binary written JSON file then we de_pickle it
for consumption!
"""


def serialize_and_save_to_file(data, filename):
    """
    this writes the binary into a JSON file
    """
    # Your code here to serialize and save data to the specified file
    pickle_out = open(filename, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()
    pass


def load_and_deserialize(filename):
    """
    this opens a JSON file with binary information and returns to the caller.
    """
    # Your code here to load and deserialize data from the specified file
    de_pickle = open(filename, "rb")
    output = pickle.load(de_pickle)
    return (output)
