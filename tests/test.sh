cat sample.csv | pit -p 'base64.encodestring(_)[:100]'
cat sample.csv | pit -d , -f '_[0].endswith("ff")'
