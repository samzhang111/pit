cat sample.csv | pit 'print len(_)'
cat sample.csv | pit -f '_.split(",")[0].endswith("ff")'
