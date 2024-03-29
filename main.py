#!/usr/bin/env python3

import sys
import signal
import math


class Groundhog:
    def __init__(self):
        self.input_value = 0.0
        self.period = 0
        self.active_period = 1
        self.temperatures = []
        self.switch = 0
        self.abberation = []
        self.average = 0.0
        self.relative = 0
        self.standard = 0.0


    def verif_input(this):
        """Get input from user and handle error cases"""
        input_value = input()
        try :
            if (input_value == "STOP"):
                return input_value
            input_value = float(input_value)
        except ValueError:
            sys.stdout.write("Invalid number give in argument\n")        
            exit(84)
        return input_value

    def verif_arg(this):
        try :
            input_value = int(sys.argv[1])
        except ValueError:
            sys.stdout.write("Invalid number give in argument\n")        
            exit(84)
        return input_value

    def set_values(this):
        this.temperatures.append(this.input_value)
        this.average = sum(this.temperatures) / len(this.temperatures) 

    def is_switch(this):
        return this.temperatures[-1] < this.temperatures[-2] if len(this.temperatures) > 1 else False

    def print_values(this):
        if this.active_period < this.period:
            average, relative, standard = float('nan'), float('nan'), float('nan')
        elif this.active_period == this.period:
            average, relative = float('nan'), float('nan')
            standard = this.standard
        else:
            average = this.average
            relative = this.relative
            standard = this.standard

        print(f"g={average:.2f}\t\tr={relative}%\t\ts={standard:.2f}\t\t{'' if not this.is_switch() else 'a switch occurs'}")

    
    def main(this):
        this.period = this.verif_arg()
        while (this.input_value != "STOP"):
            this.input_value = this.verif_input()
            this.set_values()
            this.print_values()
            this.active_period += 1
        print("Global tendency switched", this.switch, "times")
        # Add weird values
        print("5 weirdest value are [0, 0, 0, 0, 0]")

def print_help():
    print("SYNOPSIS")
    print("\t./groudhog period\n\n")
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda signum, frame: exit(84))
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            exit(print_help())
        groundhog = Groundhog()
        exit(groundhog.main())
    exit(84)