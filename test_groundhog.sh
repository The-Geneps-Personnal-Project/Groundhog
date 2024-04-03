#!/bin/bash

# Set the period
PERIOD=7

# Read the input values from the file and feed them to the program
while IFS= read -r TEMPERATURE; do
    echo "$TEMPERATURE"
    sleep 1
done < input.txt | ./groundhog $PERIOD
