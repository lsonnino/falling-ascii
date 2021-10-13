#!/usr/bin/python
import os
import sys
from time import sleep
from random import randrange
from alphabets import dict

# Config
# Probabilities are given from 0 to 9, 9 being 100%
prob_column = 2
prob_change_column = 20
speed = 10
alphabet = dict['ones']

def help():
    print("Usage:")
    print("\tpython main.py [options]")
    print("")
    print("Options:")
    print("\t--alphabet | -a | -A : Specifies an alphabet to use. See below for more information.")
    print("\t--change   | -C      : The probability from 0 to 100 that a column of chars will disapear.")
    print("\t--cols     | -c      : The probability from 0 to 100 that a column of chars will appear.")
    print("\t--help     | -h | -H : Displays this help page.")
    print("\t--speed    | -s | -S : Set the speed of the text.")
    print("")
    print("Alphabets:")
    print("Provide the value \'list\' to the alphabet argument to see what alphabets are available. " + \
    "To see the characters forming an alphabet, use \'show\' followed by the alphabet\'s name.")
    print("To specify an alphabet, provide the alphabet's name as value to the alphabet argument. To specify a custom alphabet, use the keyword \'use\' " + \
    "followed by the alphabet as a word. Every char of the word will be used. No spaces can be contained in a custom alphabet.")
    print("Here are a few examples:")
    print("\tpython main.py -a list")
    print("\tpython main.py -a show binary")
    print("\tpython main.py -a binary")
    print("\tpython main.py -a use abc")
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
    elif arg == "--alphabet" or arg == '-a' or arg == '-A':
        if len(sys.argv) == 0:
            print(f"No values given to argument \'{arg}\'")
            exit(1)
        arg = sys.argv.pop(0)

        if arg == 'list':
            for key, value in dict.items() :
                print(key)
            exit(0)
        elif arg == 'show':
            if len(sys.argv) == 0:
                print(f"No alphabets provided")
                exit(1)
            arg = sys.argv.pop(0)
            for key, value in dict.items() :
                if key == arg:
                    print(value)
                    exit(0)
            print(f"Alphabet \'{arg}\' not found")
            exit(1)
        elif arg == 'use':
            if len(sys.argv) == 0:
                print(f"No alphabets provided")
                exit(1)
            arg = sys.argv.pop(0)
            alphabet = list(arg)
        else:
            found = False
            for key, value in dict.items() :
                if key == arg:
                    alphabet = dict[arg]
                    found = True
            if not found:
                print(f"Alphabet \'{arg}\' not found. Use \'--alphabet list\' to see all available alphabets")
                exit(1)
    else:
        print(f"Unrecognised argument \'{arg}\'")
        print("Use the argument \'--help\' for help")
        exit(1)

# Shortcuts
clear_term = lambda: os.system('cls' if os.name == 'nt' else 'clear')
get_term_size = lambda: os.get_terminal_size()
get_char = lambda: randrange(len(alphabet))

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
                state.append(get_char() if randrange(100) < prob_column else -1)
        elif state_len > width:
            for i in range(state_len - width):
                state.pop()
        state_len = width

        # Get next state
        for i in range(state_len):
            if state[i] >= 0:
                state[i] = -1 if randrange(100) < prob_change_column else get_char()
            else:
                state[i] = get_char() if randrange(100) < prob_column else -1

        # Print
        print('')
        for x in range(width):
            print(alphabet[state[x]] if state[x] >= 0 else ' ', end='')

        # Wait
        sleep(1.0/speed)
except KeyboardInterrupt:
    print('')
    clear_term()
    exit(0)
