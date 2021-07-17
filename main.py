# -----------------------------
# About the Project: This is a Code written in Python to Print Green Coloured Test Passed with Tickmark Message!
# Author: Aman Chourasia
# Website: www.amanchourasia.in
# Date of Creation: 17th July 2021
# -----------------------------

# Code Starts Here!

import time # Imported Time Module

class style(): # Created a Class

    # Declaring the Colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 1 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 2 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 3 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 4 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 5 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 6 passed" + ENDC) # Printing the Output

    time.sleep(0.5) # Delay the printing statement
    print(OKGREEN + "✓ Test 7 passed" + ENDC) # Printing the Output

# Code Ends Here!
