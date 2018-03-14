#!/bin/bash

##################################################################### IMPORTANT ######################################################################
## Each new sanity test must be placed in an interval folder. If it is unknown at what interval the script should run, please store it in default.  ##
##                                                                                                                                                  ##
## The code until the comment 'END OF REQUIRED CODE' is required for the sanity test to function properly.                                          ##
##                                                                                                                                                  ##
## The 'getopts' while loop can be extended if your test has extra command line options to process, and this also requires the use of the function  ##
##   base_add_usage_argument to add that command line option to the usage/help message.                                                             ##
##                                                                                                                                                  ##
## DO NOT use exit codes 0, 1, 42, or 43 in your script. Codes 0 and 1 are automatically processed in the sanity.base file when the tests run.      ##
##   Codes 42 and 43 are reserved to reflect errors within this framework itself (the sanity.base file), like using a feature improperly. It will   ##
##   be much easier to identify where an error occurred if the developer doesn't use these exit codes.                                              ##
##                                                                                                                                                  ##
## If any parsing of the nids defined in /etc/hosts is needed please use BASE_NID_ARR, BASE_NID_LIST, BASE_NID_COUNT, and BASE_NID_LAST.            ##
##   The functionality of these are described in the helloworld script (in the support_files folder), and in the sanity.base.sh file                ##
##                                                                                                                                                  ##
## Use base_verbose_print in your script instead of the 'echo' command. This is to ensure nothing is printed to STDOUT in -q (quiet) and            ##
##   -j (JSON) modes.                                                                                                                               ##
##                                                                                                                                                  ##
## Use base_urika_sanity_print to configure what each sanity tests prints to the terminal when run via urika-sanity                                 ##
######################################################################################################################################################

# Figure out where to source the sanity.base.sh from
DIR=$(dirname "$0")
SANITY_BASE_FILE="${DIR}/../sanity.base.sh"
if [ ! -f ${SANITY_BASE_FILE} ] ; then
  (>&2 echo "You have not placed the sanity script into an appropriate folder")
  (>&2 echo "Please place it in a folder whose parent has \"sanity.base.sh\"")
  exit -1
fi
source ${SANITY_BASE_FILE}

## 'base_add_usage_argument' can be used here, refer to the instructions in the sanity.base file and the helloworld script. Example:
## base_add_usage_argument "[-z NUM]" "-z" "This is a test option, it takes a NUMber for the argument" "It still needs to be configured in 'getopts'"

## YOU MAY EXTEND THIS, BUT DO NOT CHANGE THE EXISTING DEFAULT BEHAVIOR.
# Default usage: mandatory options are -t, -v [0-n], -j, -q, -h

while getopts ":v:jqth" PRIV_BASE_X ; do
  case "${PRIV_BASE_X}" in
    v) # Verbose mode is on
      base_mode "v" "${OPTARG}"
      ;;
    j) # JSON output is enabled
      base_mode "j"
      ;;
    q) # Quiet mode is on
      base_mode "q"
      ;;
    t) # Trace mode enabled
      base_mode "t"
      set -x # Prints commands and their arguments as they are executed
      ;;
    h) # Display the usage/help message
      base_usage
      ;;
    ##
    ## Custom options to be added here after the h) option but before the *) option
    ##
    *) # Invalid input
      echo -e "\nInvalid options, check usage help.\n"
      base_usage
      ;;
  esac
done
shift $((OPTIND-1))

######################################################################################################################################################
################################################ END OF REQUIRED CODE. Develop the test from here on. ################################################
######################################################################################################################################################

# Finds the login node
base_verbose_print INFO '\nIdentifying the login node ...'
LOGIN_NOTRIM=$(/global/getglobalvar login1)
LOGIN=${LOGIN_NOTRIM##*\ } # Trim leading blanks from login node


REGEX="Active: active"
  
base_verbose_print INFO '\nChecking slapd service on login node ...\n'
  
LDAP_STATUS=$(ssh "${LOGIN}" systemctl status slapd | grep "${REGEX}" 2>/dev/null)

  base_set_test "ldap test" "lapd service running on ${LOGIN} node" "ldap service not running on ${LOGIN} node"

  if [ ! -z "$LDAP_STATUS" ] ; then
    base_update_test_state "ldap test" PASS
  else
    base_update_test_state "ldap test" FAIL
  fi

base_print