# awk

```

# write only 1st and 2nd column of file, using white space as delimiter
awk '{print $1, $2}' log.txt

# set delimiter when choosing columns
awk -F "," '{print $1, $2}' log.txt

# find lines common in all files
awk '(NR==FNR){a[$0]=1;next}
     (FNR==1){ for(i in a) if(a[i]) {a[i]=0} else {delete a[i]} }
     ($0 in a) { a[$0]=1 }
     END{for (i in a) if (a[i]) print i}' file1 file2 file3 ... file200
     
# filtering rows based on a condition
awk '$4 > 169' data.txt

# printing lines containing specific word
awk '/John/' data.txt

# Find dupe files
# Create the SQLite database and table
sqlite3 files.db "CREATE TABLE files (path TEXT, md5 TEXT, mod_date TEXT);"

# Import the CSV data into the SQLite table
sqlite3 files.db <<EOF
.mode csv
.import output.csv files
EOF

# Query the database for duplicates and sort the results
sqlite3 files.db <<EOF
.mode csv
.output duplicates_sorted.csv
SELECT path, md5, mod_date
FROM files
WHERE md5 IN (
    SELECT md5
    FROM files
    GROUP BY md5
    HAVING COUNT(md5) > 1
)
ORDER BY md5, mod_date;
EOF

# look at csv results
cat duplicates_sorted.csv

# Remove duplicate lines and save the rest into a new file
awk ‘!seen[$0]++’ filename > newfile

```

# bash

```

# compares the sorted versions of two files without creating intermediate files
diff <(sort file1.txt) <(sort file2.txt)

# enable globstar and list all text files in dirs and subdirs
shopt -s globstar
ls **/*.txt

# enable extglob and delete all files except those ending with .txt

shopt -s extglob
rm !(*.txt)

# combine pdfs
pdftk file1.pdf file2.pdf cat output combined.pdf

```

# cmd

```

# compare two files and print lines with diffs
FC file1.ext file2.ext

# compare multiple files
comp log1.txt log2.txt log3.txt

# find all lines with search term in a file
find "type" header-compare.csv

# sort file
sort sample.txt

# view contents page by page
more long_text.txt

# clear screen
cls

# display or set date
date

# rename files
ren header-compare-PC-010536.csv header-compare-saved.csv

# display or set time
time

# move files from one dir to another
move 

# display tree structure of dir
tree

# display all active system tasks
tasklist

# kill active system task by calling the task id
taskkill /pid 1234

# test system connectivity
ping

```

# jq

```

# parse 
for file in *.json; do
    jq 'select(.SalesforceResponse != null) | del(.salesforce_response_metrics, .input_file) | .SalesforceResponse as $sf | del(.SalesforceResponse) | . + $sf' "$file" > "filtered_$file"
done

# convert to csv
jq -r '(.[0] | keys_unsorted) as $keys | $keys, map([.[ $keys[] ]])[] | @csv' filtered_*.json > combined_output.csv

```

# sed

```

#remove double quotes from title tag
sed -i.bak 's/^title: "\([^"]*\)"/title: \1/' *.md
sed -i.bak 's/^date: "\([^"]*\)"/title: \1/' *.md
rm *.bak

#Add new line to front matter
sed -i.bak '/^tags:/a\
layout: post
' *.md

# To remove bak files
rm *.bak

# substituting string with replacement in file.txt
sed 's/old/new/' file.txt

# convert all lowercase letters to uppercase in textfile.txt
sed 's/.*/\U&/' textfile.txt

```

# zsh

## Globbing

### regular
```
# Match all .txt files in the current directory
*.txt

# Match files like file1.txt, file2.txt, etc., in the current directory
file?.txt

# Match all .txt files recursively within directories
**/*.txt

# move all jpg and png files to specific dir
cp *.{jpg,png} images/

# Change the extension of filename from .txt to .md
${filename%.txt}.md

# Convert a filename variable to lowercase
${file:l}
```

### extended globbing

```

Enable extended globbing with the following command:

setopt EXTENDED_GLOB

ls *(.) - List only regular files.
ls *(/) - List only directories.
ls *(-/) - List only directories and symbolic links to directories.

```

### find

```

# find all gif files in a dir or subdir 
find . -type f -name '*.gif' -exec sh -c \
'file "$0" | grep -q "animated"' {} \; -print

```

### wordcount

```

# count number of lines in file
wc -l filename

```