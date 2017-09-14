# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 04:35:31 2016

@author: Animesh Kumar Jha
"""

import json
import csv



json_dt = open('invoicelineitems-87349685-1497505549.20170615102538.json')
json_resp = json.load(json_dt)

data = json_resp['data']

"""

with open('db_coloumns', "rb") as infile:
    in_txt = csv.reader(infile)
    outfile = open('output_csv.csv', 'wb+')
    out_csv = csv.writer(outfile)
    out_csv.writerows(in_txt)
    
json_data = open('invoicelineitems-87349685-1497505549.20170615102538.json').read()
myData = json.load(json_data)
#print myData

cost_data = myData['data']

#print cost_data['data']['instanceId']

csv_file = csv.writer(open("test.csv", "wb+"))

csv_file.writerow(["instanceId", "serviceAdministratorId", "resourceLocation", "cost", "meterName"])
"""


"""for key in cost_data:
    print key"""



with open('test_with_dict.csv', 'w') as csv_file:
#    fieldnames = ['providerName', 'assetAccountId','billingAccountId','providerRegion','assetName','providerAssetId']
    with open('db_coloumns', "rb") as db_cols_txt:
        headers = db_cols_txt.read().splitlines()
        print headers

        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()

        for row in data:
            writer.writerow({'providerName': 'azure ASM',
                         'assetAccountId': row["accountId"],
                         'billingAccountId':row["accountId"],
                         'providerRegion':row["resourceLocation"],
                         'assetName':row["instanceId"],
                         'providerAssetId':row["instanceId"]})








"""csv_file = csv.writer(open("test.csv", "wb+"))
csv_file.writerow(["instanceId", "serviceAdministratorId", "resourceLocation", "cost", "meterName"])"""

"""for row in data:
    csv_file.writerow([row["instanceId"],
                       row["serviceAdministratorId"],
                       row["resourceLocation"],
                       row["cost"],
                       row["meterName"]])"""




