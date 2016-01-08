# Zach Brown
# xzachx@alum.wpi.edu
# rss_grouper.py

import csv
import feedparser
from urlparse import urlparse

with open('feed_list.tsv', 'rb') as input:
    reader = csv.reader(input, delimiter='\t')
    next(reader, None)
    urls = dict()
    for line in reader:
        url = line[1:][0]
        parsed_url = urlparse(url)
        base_url = '{url.scheme}://{url.netloc}/'.format(url=parsed_url)

        if base_url not in urls:
            urls[base_url] = {url}
            
        else:
            urls[base_url].add(url)

# Determine anagram with the most instances
most_urls = max(urls, key=lambda k: len(urls[k]))

# Determine number of instances for the most used anagram
most_urls_count = len(url[most_urls])
 
#for url in urls:    
#    parsed_url = feedparser.parse(url)
#    try:
#        print parsed_url['feed']['title']
#    except KeyError:
#        pass