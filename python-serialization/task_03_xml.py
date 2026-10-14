#!/usr/bin/env python3

import xml.etree.ElementTree as ET
"""
functions that convert csv data into json file
"""


def serialize_to_xml(dictionary, filename):
    """
    this writes the dictionary into a xml file
    """
    try:
        root = ET.Element("data")
        for key, val in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(val)

        tree = ET.ElementTree(root)
        with open(filename, "wb") as xml:
            tree.write(xml)

    except IOError, EOFError:
        print("uh oh, problems")


def deserialize_from_xml(filename):
    """
    this reads the xml file into a dictionary
    """
    try:
        output = {}
        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root:
            output.update({child.tag:child.text})

        return (output)

    except IOError, EOFError:
        return (None)
