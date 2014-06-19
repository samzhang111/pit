cat sample.csv | pit 'len(_)'
cat sample.csv | pit -d , -f '_[0].endswith("ff")'

#equivalent of cat sample.csv | awk 'BEGIN { FS="," }{ PRINT $1; }' | sort | uniq | wc:
cat sample.csv | pit -d , -e -b 'a=set()' 'a.add(_[0])' 'print len(a)'
