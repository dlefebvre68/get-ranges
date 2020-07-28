#!/usr/bin/python3

import json
import sys
import os.path

if len(sys.argv) < 3:
    print("usage: " + sys.argv[0] + " <file to download> [<region> [<region>]]")
    exit(1)

filename = os.path.basename(sys.argv[1])
regions = []

for region in sys.argv[2:]:
    regions.append(region)

with open(filename, 'r') as fd:
    ranges = json.load(fd)

    for range in ranges["prefixes"]:
        if len(regions) == 0:
            print(range["ip_prefix"])
        else:
            for region in regions:
                if range["region"] == region:
                    print(range["ip_prefix"])
fd.close()
