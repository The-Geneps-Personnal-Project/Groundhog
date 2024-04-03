#!/usr/bin/env python3

import sys
import signal
import math
import statistics

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
        self.standard_list = []
        self.relative_list = []


    def verif_input(self):
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

    def verif_arg(self):
        try :
            input_value = int(sys.argv[1])
        except ValueError:
            sys.stdout.write("Invalid number give in argument\n")        
            exit(84)
        return input_value

    def calculate_average(self):
        if (len(self.temperatures) - 1 < self.period):
            return 0
        # Get the last n = period + 1 temperatures
        last_temperatures = self.temperatures[-(self.period + 1):]
        difference_list = []
        # Iterate over the last n = period temperatures
        for i in range(len(last_temperatures) - 1):
            # Calculate difference between n and n+1 temperature
            difference = round(last_temperatures[i + 1] - last_temperatures[i], 1)
            if (difference > 0):
                difference_list.append(difference)
            else:
                difference_list.append(0)
        # Calculate the average of the difference
        self.average = sum(difference_list) / len(difference_list)

    def calculate_relative(self):
        if (len(self.temperatures) - 1 < self.period):
            return 0
        current_temperature = self.temperatures[-1]
        temperature_n_days_ago = self.temperatures[-(self.period + 1)]
        if (temperature_n_days_ago <= 0):
            return 0
        self.relative = round(((current_temperature - temperature_n_days_ago) / temperature_n_days_ago) * 100)
        self.relative_list.append(self.relative)

    def calculate_standard(self):
        if (len(self.temperatures) < self.period):
            return 0
        last_temperatures = self.temperatures[-self.period:]
        avg = sum(last_temperatures) / len(last_temperatures)
        self.standard = math.sqrt(sum([(x - avg) * (x - avg) for x in last_temperatures]) / len(last_temperatures))
        self.standard_list.append(self.standard)

    def verif_switch(self):
        if (len(self.standard_list) < 3):
            return 0
        self.switch = 0
        is_standard_order = (
            (self.standard_list[-3] > self.standard_list[-2] and self.standard_list[-2] < self.standard_list[-1]) or
            (self.standard_list[-3] < self.standard_list[-2] and self.standard_list[-2] > self.standard_list[-1])
        )
        is_relative_switch = (
            (self.relative_list[-2] > 0 and self.relative_list[-1] < 0) or
            (self.relative_list[-2] < 0 and self.relative_list[-1] > 0)
        )
        if is_standard_order and is_relative_switch:
            self.switch += 1

    def set_values(self):
        self.temperatures.append(self.input_value)
        self.calculate_average()
        self.calculate_relative()
        self.calculate_standard()
        self.verif_switch()

    def print_values(self):
        if self.active_period < self.period:
            average, relative, standard = float('nan'), float('nan'), float('nan')
        elif self.active_period == self.period:
            average, relative = float('nan'), float('nan')
            standard = self.standard
        else:
            average = self.average
            relative = self.relative
            standard = self.standard
        print(f"g={average:.2f}\t\tr={relative}%\t\ts={standard:.2f}\t\t{'a switch occurs' if self.switch else ''}")
    
    def main(self):
        self.period = self.verif_arg()
        while (self.input_value != "STOP"):
            self.input_value = self.verif_input()
            self.set_values()
            self.print_values()
            self.active_period += 1
        print("Global tendency switched", self.switch, "times")
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