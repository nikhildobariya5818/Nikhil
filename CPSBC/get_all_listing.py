import json
import os


def json_in_output():
    data = []
    x = os.listdir("Output")
    print(len(x))
    for filename in x:
        with open('Output/' + filename, encoding='utf-8') as json_data:
            data += json.load(json_data)
    listing_urls = []
    for url in data:
        listing_urls.append(url)
    listing_urls = list(set(listing_urls))
    print(len(listing_urls))
    with open('All_listing.json', 'w', encoding='utf-8') as outfile:
        json.dump(listing_urls, outfile, indent=4)


json_in_output()