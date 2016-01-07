# Zach Brown
# xzachx@alum.wpi.edu
# rss_grouper.py

import csv
import feedparser

with open('feed_list.tsv', 'rb') as input:
    reader = csv.reader(input, delimiter='\t')
    next(reader, None)
    urls = []
    for line in reader:
        urls += line[1:]
    
parsed_url = feedparser.parse(urls[0])
print parsed_url