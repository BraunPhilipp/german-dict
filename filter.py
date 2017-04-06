# -*- coding: utf-8 -*-

import json
import string
import csv

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

noun_list = []
with open('dict.txt', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        #print(row)
        row[0] = row[0].lower()
        if "ADJ" in row[2] and hasNumbers(row[0]) == False and "-" not in row[0] and "." not in row[0] and "ö" not in row[0] and "ä" not in row[0] and "ü" not in row[0] and "/" not in row[0] and len(row[0]) < 8 and len(row[0]) > 2:
            noun_list.append(row[0])
            print(row[0].replace("ß","ss"))
