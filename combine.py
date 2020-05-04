"""
Finally create a script called combine.py which iterates over the resulting json files and
 generates a single csv of all products with the following fields:

prod_id,prod_sku,prod_cat,prod_name 
"""

import os
import csv
import json


f2 = open('output.csv', 'w')
f2.write("prod_id,prod_sku,prod_cat,prod_name\n")
f2.close()

f2 = open('output.csv', 'a')

writer = csv.writer(f2, delimiter=',', lineterminator='\n')

for root, dirs, files in os.walk('out'):
    #print(root, dirs, files)
    path = root.split(os.sep)
    for fn in files:
        fp = root + os.sep + fn
        print("Reading from the File: " + fp)

        # Opening JSON file
        with open(fp, 'r') as openfile:

            # Reading from json file
            json_dict = json.load(openfile)

            # print(json_dict)
            prod_id = json_dict['prod_id']
            prod_sku = json_dict['prod_sku']
            prod_cat = json_dict['prod_cat']
            prod_name = json_dict['prod_name']
            row = [prod_id, prod_sku, prod_cat, prod_name]

            writer.writerow(row)
            print("Successfully wrote the File:" + fp + " to output.csv")
f2.close()
