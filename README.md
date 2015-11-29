# Dateify
These scripts add date pages to the wiki.

## datefacts.py
`datefacts.py` accepts as its argument a list of paths which should be articles in the wiki, e.g., `datefacts.py ../import/*.html` and outputs a line delimited list of sentences featuring a year. In essence, it reads the contents of each file passed to it, tries to split the contents into a list of sentences, filters out sentences that do not contain a four-digit number, and, if it's an article about a person, attempts to dereference pronouns by replacing them with the person's name. 

You can generate a file containing all datefacts like so:
```bash
python datefacts.py ../encyclopedia-brunoniana/*.html > datefacts.txt
```

## datefacts.sh
`datefacts.sh` reads from `datefacts.txt` (a file containing all datefacts) adds each fact to the file representing each year mentioned in the fact). To run:

```bash
bash ./dateify.sh
```
