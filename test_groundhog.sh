#!/bin/bash

# Set the number of iterations
ITERATIONS=17

# Set the period
PERIOD=7

# Run the program in a loop
for ((i=0; i<$ITERATIONS; i++)); do
    # Read the input values from the file and feed them to the program
    while IFS= read -r TEMPERATURE; do
        echo "$TEMPERATURE"
        sleep 1
    done < input.txt
done | ./groundhog $PERIOD
