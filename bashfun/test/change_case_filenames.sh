#!/bin/bash

usage() { echo "Usage: $0 --case <upper | lower>" 1>&2; exit 1;}


#eval set -- `getopt --long case:, help -o c:h: -- "$@"`

while [ $# -gt 0 ]
do
  case "$1" in
    -c | --case)
       switchcase="$2" ;
       shift 2;;
    -h | --help)
       usage ;
       exit 0 ;;
    -*)
       echo "Error: Invalid option: $1" >&2
       usage;
       exit 1;;  
   esac

#DIR = "/Users/c17625/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/heyjude/bashfun/test/"
#cd $DIR 

  if [ $switchcase = "upper" ]; then
    echo "\changing filename to uppercase...";
    for i in *; do mv $i `echo $i | tr [:lower:] [:upper:]`; done;
    ls -ll 
  elif [ $switchcase = "lower" ]; then
    echo "\changing filename to lowercase...";
    for i in *; do mv $i `echo $i | tr [:upper:] [:lower:]`; done;
    ls -ll
  else
    echo "Error: try again!"
    usage
    exit 1
  fi

done
