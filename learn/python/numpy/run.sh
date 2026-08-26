#!/bin/bash

output=$(python "$1" 2>&1)
echo $(echo "$output" | grep "execute time")
time=$(echo "$output" | grep "execute time" | sed -E 's/^.*execute time:\s*([0-9.]+)$/\1/')
echo "$time" > time.csv