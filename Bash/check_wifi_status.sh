#!/bin/bash
set -xeu

repo_dir="/Users/vsanghvi/p-repos"
py_repo=$repo_dir/heyjude/Python
docker_repo=$repo_dir/docker-stuff

#cd $docker_repo/smtp/
#./docker-cleanup-postfix.sh

cd $docker_repo/smtp/
./docker-run-postfix.sh

cd $py_repo/
source ./local_smtp.env

cd $py_repo/wip/
python internet_speed_test.py

cd $docker_repo/smtp/
./docker-cleanup-postfix.sh
