#!/bin/bash
myfile=$1
if [ -f $myfile ]
then
echo "$myfile exists"
fi
exit 0

