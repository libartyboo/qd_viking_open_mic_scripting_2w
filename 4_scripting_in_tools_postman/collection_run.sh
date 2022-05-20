#!/bin/bash

collectionName=RestCountries_4_nm.postman_collection.json

devEnv=env_dev_RestCountries.postman_environment.json
stageEnv=env_stage_RestCountries.postman_environment.json
prodEnv=env_prod_RestCountries.postman_environment.json

envList=("${prodEnv} ${stageEnv} ${devEnv}")
envfList=('prod' 'stage' 'dev' 'all')

echo "script accept next parameters: "
echo "-prod"
echo "-stage"
echo "-dev"
echo "-all"

if [[ "$1" = "-prod" ]]; then
    env=$prodEnv
    envf=prod
elif [[ "$1" = "-stage" ]]; then
    env=$stageEnv
    envf=stage
elif [[ "$1" = "-dev" ]]; then
    env=$devEnv
    envf=dev
else
    env=$devEnv
    envf=dev
fi

if [[ "$1" = "-all" ]]; then
    i=1
    for environment in $envList
    do
    timeM=$(date +%Y%m%d-%H%M%S)
    file=api_run_${envfList[$i-1]}_${timeM}.txt
    i=$(($i+1))
    newman run $collectionName -e $environment >> reports/$file
    done
    
else
    timeM=$(date +%Y%m%d-%H%M%S)
    file=api_run_${envf}_${timeM}.txt
    newman run $collectionName -e $env | tee reports/$file
fi
