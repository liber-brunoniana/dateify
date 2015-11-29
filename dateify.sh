#!/bin/bash

rm -rf ./build/*
mkdir ./build

# Generate date pages from the contents of datefacts.txt
cat datefacts.txt | while read line; do
  dates=`echo $line | grep -o "\<[[:digit:]][[:digit:]][[:digit:]][[:digit:]]\>" | sort | uniq`
  echo "$dates" | while read date; do
    echo "<li>$line</li>" >> "./build/$date.html"
  done
done

# Wraps the lists with <ul> elements.
find ../import/ -name "[[:digit:]][[:digit:]][[:digit:]][[:digit:]].html" -print0 | while IFS= read -r -d '' file; do
	contents=`cat $file`
  echo $file
  echo "<ul>$contents</ul>" > "./build/$file" 
done
