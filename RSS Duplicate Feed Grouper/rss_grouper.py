# Zach Brown
# xzachx@alum.wpi.edu
# rss_grouper.py

# Import libraries for reading/writing tsv files and parsing urls
import csv
from urlparse import urlparse

# Read in feed list tsv file
with open('feed_list.tsv', 'rb') as input:
    reader = csv.reader(input, delimiter='\t')
    
    # Skip header row
    next(reader, None)
    
    # Initialize dictionary to read feeds into
    urls = dict()
    
    # Read feeds into urls dictionary
    for line in reader:
        
        # Strip off feed id from line
        url = line[1:][0]
        
        # Strip off parameters to get the base url
        parsed_url = urlparse(url)
        base_url = '{url.scheme}://{url.netloc}{url.path}'.format(url=parsed_url)

        # Add key/value entry for the base url in the dictionary if it doesn't exist
        if base_url not in urls:
            urls[base_url] = {url}
        
        # Otherwise, append the url for the list in the value for the base url
        else:
            urls[base_url].add(url)

# Write the output to a new tsv file
with open('feed_groupings.tsv', 'wb') as output:
    
    # Write the header row
    output.write('Base_Url\tFeed\n')
    
    # Iterate through each key in the dictionary
    for url in urls:
        
        # Iterate through each list entry in the value for the given key
        for feed in urls[url]:
            
            # Write the base url and feed url to the output file
            output.write('%s\t%s\n' % (url, feed))
           
