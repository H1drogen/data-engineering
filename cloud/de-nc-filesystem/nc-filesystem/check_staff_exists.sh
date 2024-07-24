#!/bin/bash

staff_id=$1
file_name="./staff/nc-${staff_id}.json"

if [ -f "$file_name" ]; then
    echo "Staff file ${staff_id} found"
else
    echo "Staff file ${staff_id} not found"
fi