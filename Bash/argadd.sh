#!/bin/bash

if [ $# -ne 2 ]
then
echo "Usage: $0   x  y"
echo " where x and y are the integer number we need to add "
exit 1
fi

echo "sum of two numbers: `expr $1 + $2`"

