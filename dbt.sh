#!/bin/bash

args_length=${#@}

export DBT_PROJECT_DIR=$PWD/dbt/sampleproject
export DBT_PROFILES_DIR=$PWD/dbt/profiles
if [ $args_length -eq 0 ]; then
     python3 dbt/runner/main.py
else
    set -x
    python3 dbt/runner/main.py $@ --project-dir $DBT_PROJECT_DIR --profiles-dir $DBT_PROFILES_DIR
fi
