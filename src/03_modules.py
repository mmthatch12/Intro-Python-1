"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)
# if len(sys.argv) > 1:
#     for arg in sys.argv:
#         print(arg)
# else:
#     print('No args provided')
# Print out the OS platform you're using:
# YOUR CODE HERE
print("windows version?", sys.getwindowsversion().platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version?", sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
print("current process id", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("current working dir", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("login name", os.getlogin())
