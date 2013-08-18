#!/bin/bash 

# List all of the users on the system 
# in alphabetical order

lastlog | cut -d' ' -f1 | sort
