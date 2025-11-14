# Python Modules


# The concept of module in Python further enhances the modularity.
# You can define more than one related functions together and load required functions.
# A module is a file containing definition of functions, classes, variables, constants or any other Python object.
# Contents of this file can be made available to any other program. Python has the import keyword for this purpose.
'''

Python Built In Modules
#
# 1
#
# os
#
# This module provides a unified interface to a number of operating system functions.
#
# 2
#
# string
#
# This module contains a number of functions for string processing
#
# 3
#
# re
#
# This module provides a set of powerful regular expression facilities. Regular expression (RegEx), allows powerful string search and matching for a pattern in a string
#
# 4
#
# math
#
# This module implements a number of mathematical operations for floating point numbers. These functions are generally thin wrappers around the platform C library functions.
#
# 5
#
# cmath
#
# This module contains a number of mathematical operations for complex numbers.
#
# 6
#
# datetime
#
# This module provides functions to deal with dates and the time within a day. It wraps the C runtime library.
#
# 7
#
# gc
#
# This module provides an interface to the built-in garbage collector.
#
# 8
#
# asyncio
#
# This module defines functionality required for asynchronous processing
#
# 9
#
# Collections
#
# This module provides advanced Container datatypes.
#
# 10
#
# functools
#
# This module has Higher-order functions and operations on callable objects. Useful in functional programming
#
# 11
#
# operator
#
# Functions corresponding to the standard operators.
#
# 12
#
# pickle
#
# Convert Python objects to streams of bytes and back.
#
# 13
#
# socket
#
# Low-level networking interface.
#
# 14
#
# sqlite3
#
# A DB-API 2.0 implementation using SQLite 3.x.
#
# 15
#
# statistics
#
# Mathematical statistics functions
#
# 16
#
# typing
#
# Support for type hints
#
# 17
#
# venv
#
# Creation of virtual environments.
#
# 18
#
# json
#
# Encode and decode the JSON format.
#
# 19
#
# wsgiref
#
# WSGI Utilities and Reference Implementation.
#
# 20
#
# unittest
#
# Unit testing framework for Python.
#
# 21
#
# random
#
# Generate pseudo-random numbers
#
# 22
#
# sys
#
# Provides functions that acts strongly with the interpreter.
#
# 23
#
# requests
#
# It simplifies HTTP requests by offering a user-friendly interface for sending and handling responses.
#
# 24
#
# itertools
#
# An iterator object is used to traverse through a collection (i.e., list, tuple etc..). This module provides various tools which are used to create and manipulate iterators.
#
# 25
#
# locale
#
# The locale module in Python is used to set and manage cultural conventions for formatting data. It allows programmers to adapt their programs to different languages and regional formatting standards by changing how numbers, dates, and currencies are displayed.
#


'''

import math

print("Square root of 100: ", math.sqrt(100))




# Python User-defined Modules


# Creating a Python Module

# Creating a module is nothing but saving a Python code with the help of any editor. Let us save the following code as mymodule.py
# def SayHello(name):
#    print ("Hi {}! How are you?".format(name))
#    return




import mymodule

mymodule.SayHello("Karmanya")



# from modname import *
# from modulename as alias

#
# import mymodule as x
# print ("sum:",x.sum(10,20))
# print ("average:", x.average(10,20))
# print ("power:", x.power(10, 2))





# Locating Modules
# When you import a module, the Python interpreter searches for the module in the following sequences −
#
# The current directory.
#
# If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.
#
# If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.
#

# The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.
#

# The PYTHONPATH Variable
# The PYTHONPATH is an environment variable, consisting of a list of directories. The syntax of PYTHONPATH is the same as that of the shell variable PATH.
#
# Here is a typical PYTHONPATH from a Windows system −
#
# set PYTHONPATH = c:\python20\lib;
# And here is a typical PYTHONPATH from a UNIX system −
#
# set PYTHONPATH = /usr/local/lib/python


