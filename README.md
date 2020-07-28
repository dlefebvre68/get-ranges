# get-ranges
Extracts from the ip-ranges.json file published by AWS the IP ranges specific to zones.

Very simple Python3 script that takes 2 arguments.  The first is the name of the file that contains the IP ranges as per the format published by AWS; the next arguments are the zones we are interested in.

The output is a list of CIDR, one per line.
