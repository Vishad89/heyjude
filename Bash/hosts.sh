#!/bin/sh

set -eu 

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

usage() {
 echo "Usage: $0 20"
 echo "Provide host entry to be deleted"
 echo "i.e. 20, 40, etc..."
}

if [ $# -eq 0 ]; then
	usage 
	exit 1
elif [ "$1" == "-h" ]; then 
	usage
	exit 0 
elif [[ $1 =~ ^[0-9] ]]; then
	sed -i "" $1d ~/.ssh/known_hosts	
        echo "Host entry at line ${red}$1${reset} deleted"
else
	usage
	exit 1
fi
