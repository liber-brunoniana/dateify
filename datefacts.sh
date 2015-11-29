#/bin/sh

FACTS="`python -W ignore datefacts.py ../import/*,*.html | shuf`"
IFS=''
while read -u 3 -r line; do
    echo $line | cowsay & read
done 3<<< $FACTS 
