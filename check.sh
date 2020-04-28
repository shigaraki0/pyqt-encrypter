#!/bin/bash


file=$2

filename=$(basename "${file}")

output_file="$(dirname "${file}")/${filename%.*}"

#script arguments

if [ "$1" == "-c" ]
   then
       gpg -c $file 
elif [ "$1" == "-d" ]
   then
       gpg -d $file > $output_file
fi

#end of argument check
