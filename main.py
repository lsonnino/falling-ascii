#!/usr/bin/python
import os
import sys
from time import sleep
from random import randrange

# Config
# Probabilities are given from 0 to 9, 9 being 100%
prob_column = 2
prob_change_column = 20
speed = 10

def help():
    print("Usage:")
    print("\tpython main.py [options]")
    print("")
    print("Options:")
    print("\t--change  | -C      : The probability from 0 to 100 that a column of chars will disapear.")
    print("\t--cols    | -c      : The probability from 0 to 100 that a column of chars will appear.")
    print("\t--help    | -h | -H : Displays this help page.")
    print("\t--speed   | -s | -S : Set the speed of the text.")
    print("")

# Parse args

def get_number_arg(check, name, message, is_float=False):
    if len(sys.argv) == 0:
        print(f"No values given for argument {name}")
        exit(1)

    arg = sys.argv.pop(0)

    try:
        if is_float:
            tmp = float(arg)
        else:
            tmp = int(arg)
    except ValueError:
        print(f"Invalid " + ("float" if is_float else "integer") + f" value \'{arg}\': " + message)
        exit(1)

    if not check(tmp):
        print(f"Invalid " + ("float" if is_float else "integer") + f" value \'{arg}\': " + message)
        exit(1)

    return tmp


# The first arg is just the name of the file
arg = sys.argv.pop(0)
# Get the next ones
while len(sys.argv) > 0:
    arg = sys.argv.pop(0)
    if arg == '--help' or arg == "-h" or arg == '-H':
        # Display help
        help()
        exit(0)
    elif arg == '--speed' or arg == "-s" or arg == '-S':
        # Get speed
        speed = get_number_arg(
            lambda val: val > 0,
            arg,
            "this value must be strictly positive",
            is_float = True
        )
    elif arg == '--cols' or arg == "-c":
        # Get columns
        prob_column = get_number_arg(
            lambda val: val >= 0 and val <= 100,
            arg,
            "this value must be between 0 and 100",
            is_float = False
        )
    elif arg == '--change' or arg == "-C":
        # Get columns
        prob_change_column = get_number_arg(
            lambda val: val >= 0 and val <= 100,
            arg,
            "this value must be between 0 and 100",
            is_float = False
        )
    else:
        print(f"Unrecognised argument \'{arg}\'")
        print("Use the argument \'--help\' for help")
        exit(1)

# Shortcuts
clear_term = lambda: os.system('cls' if os.name == 'nt' else 'clear')
get_term_size = lambda: os.get_terminal_size()

state = []
state_len = 0

# Main loop
try:
    while (True):
        # Reset
        # clear_term()
        width, height = get_term_size()

        # Add or remove columns
        if state_len < width:
            for i in range(width - state_len):
                state.append(1 if randrange(100) < prob_column else 0)
        elif state_len > width:
            for i in range(state_len - width):
                state.pop()
        state_len = width

        # Get next state
        for i in range(state_len):
            if state[i] == 1:
                state[i] = 0 if randrange(100) < prob_change_column else 1
            else:
                state[i] = 1 if randrange(100) < prob_column else 0

        # Print
        print('')
        for x in range(width):
            print('1' if state[x] == 1 else ' ', end='')

        # Wait
        sleep(1.0/speed)
except KeyboardInterrupt:
    clear_term()
