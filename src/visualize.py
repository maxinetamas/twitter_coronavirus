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
x = []
y = []
for item in top_items:
    x.append(item[0])
    y.append(item[1])

# create a bar graph using plt.bar()
plt.bar(x, y)

# set the labels for the axes
plt.xlabel('Count')
plt.ylabel('Input')
plt.title("Input x Count")

# show the plot
plt.savefig('output.png')
plt.show()
