#!/usr/bin/env python3

# command line args
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values (edited for bar graph)
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
# get the top 10 items
top_items = items[:10]

# create lists for the x and y values
top_items = items[:10] 
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]
keys = keys[::-1]
values = values[::-1]

# plot the bar graph
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)

# set the labels for the axes
plt.xlabel('Count')
plt.ylabel('Input')
plt.title("Input x Count")

# save the bar graph as a PNG file
if args.input_path[-1] == 'g':
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.savefig(args.key[1:] + '_country.png')
