#!/bin/bash
declare -A capitals # declaring empty array
capitals[India]="New Delhi"
capitals[France]="Paris"
capitals[Japan]="Tokyo"

## Access
echo "Capital of Japan is ${capitals[Japan]}"

##Iterate for accessing Values
for capital in "${capitals[@]}"; do
    echo "$capital"
done

## Iterate with Key Value Both
# ! expands keys
for country in "${!capitals[@]}"; do
    echo "$country: ${capitals[$country]}"
done

# create array directly with values
# Amnother Way of Declaration
declare -A testArray=([India]="New Delhi" [France]="Paris" [Japan]="Tokyo" )
echo "${testArray[India]}"