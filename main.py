#!/usr/bin/env python3

import sys
import signal
import math


class Groundhog:
    def __init__(self):
        self.period = 0
        self.switch = 0
        self.abberation = []
        self.average = 0
        self.relative = 0
        self.standard = 0


def verif_input():
    """Get input from user and handle error cases"""
    input_value = input(">")
    try :
        if (input_value == "STOP"):
            return input_value
        input_value = float(input_value)
    except ValueError:
        sys.stdout.write("Invalid number give in argument\n")        
        exit(84)
    return input_value

def verif_arg():
    try :
        input_value = int(sys.argv[1])
    except ValueError:
        sys.stdout.write("Invalid number give in argument\n")        
        exit(84)
    return input_value

def handle_input(input_value):
    pass

def main(groundhog):
    groundhog.period = verif_arg()
    input_value = verif_input()
    while (input_value != "STOP"):
        print("loop")
        handle_input(input_value)
        input_value = verif_input()
    print(input_value)
    print("Global tendency switched", groundhog.switch, "times")
    # Add weird values
    print("5 weirdest value are [0, 0, 0, 0, 0]")

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        sys.exit(84)

def print_help():
    print("SYNOPSIS")
    print("\t./groudhog period\n\n")
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print_help()
            exit(0)
        #logic
        groundhog = Groundhog()
        main(groundhog)
        exit(0)
    exit(84)