#!/bin/bash

read -p "Enter the name of a file or directory: " name

if [ -f "code/$name" ]; then
    echo "$name is a file."
elif [ -d "code/$name" ]; then
    echo "$name is a directory."
    echo "Contents of $name:"
    ls "code/$name"

else
    echo "$name does not exist in code directory."
fi