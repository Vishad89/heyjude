#!/bin/sh

set -x
set -eu

if [ $# -lt 3 ]; then
    echo "provide cmd line args"
    exit 1
else
    var1=$1
    var2=$2
    var3="${@:3}"
fi

echo $var1 $var2 $var3
