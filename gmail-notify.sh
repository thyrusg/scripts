#!/bin/bash

# Setup an infinite loop
while [ 1 ]; do
    notify-send -i ~/Pictures/network-gmail.png "Unread Email" "`gmail.py`"
    # Have the program sleep for 10 minutes 
    sleep 10m
done 
