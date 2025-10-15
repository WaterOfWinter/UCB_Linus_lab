#!/bin/bash

ping -c 5 $1 > /dev/null 2> /dev/null

if [[ $? -ne 0 ]]; then 
    echo "Host is not reachabley"
else
    echo "OK"
fi

