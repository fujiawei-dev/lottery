'''
Date: 2021.09.01 14:32
Description : Omit
LastEditors: Rustle Karl
LastEditTime: 2021.09.01 15:14:21
'''
from collections import Counter
import json

with open('assets/records.txt', encoding='utf-8') as fp:
    lines = fp.readlines()

total = len(lines)

red_counter = Counter()
blue_counter = Counter()

for line in lines:
    _, reds, blue = line.strip().split(';')

    blue_counter[blue] += 1
    for red in reds.split(','):
        red_counter[red] += 1

json.dump(dict(red_counter.most_common()),
          fp=open('assets/count_red.json', 'w'), indent=2)

json.dump(dict(blue_counter.most_common()),
          fp=open('assets/count_blue.json', 'w'), indent=2)
