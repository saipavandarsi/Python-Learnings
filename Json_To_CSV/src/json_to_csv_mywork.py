# -*- coding: utf-8 -*-
"""
Created on Mon Jul 3 11:35:31 2017

@author: Shruthi Madishetty
"""

import json
import datetime
import os
import csv
import zipfile


def parse_response_to_gpd():
    json_dt = open('invoicelineitems-87349685-1497505549.20170615102538.json')
    json_resp = json.load(json_dt)
    data = json_resp['data']

    currency_dt = open('currency_code.json')
    currency_json_resp = json.load(currency_dt)

    now = datetime.datetime.now()
    start_month = datetime.datetime(now.year, now.month, 1)
    start_month = datetime.datetime.strftime(start_month, '%Y%m%d')

    #constants
    _period = '201703'
    _providerNm = 'Azure'
    _providerInvoiceId = 'estimated'
    _pcProviderTaxCost = 0.0
    _customerConversionRate = 1.0000000000

    extractDateStr = os.path.basename('invoicelineitems-87349685-1497505549.20170615102538.json')
    extractdate = extractDate = datetime.datetime.strptime((extractDateStr.split(".")[1]), '%Y%m%d%H%M%S')
    print start_month
    print str(extractdate)

    filename1 = datetime.datetime.now().strftime("%Y-%m-%d")
    filename1 = 'C_' + filename1 + '112233'

    with open(filename1 + '.csv', 'w') as csv_file:
    #    fieldnames = ['providerName', 'assetAccountId','billingAccountId','providerRegion','assetName','providerAssetId']
        with open('db_coloumns', "rb") as db_cols_txt:
            headers = db_cols_txt.read().splitlines()

            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()

            for row in data:
                writer.writerow({
                                'period': _period,                                          #1
                                'providerRecordId': "",                                     #2
                                'extractDate': extractdate,                                 #3 -- TODO more
                                'serviceStartDate': "",                  #4
                                'serviceEndDate': "",                                       #5
                                'invoiceStartDate': start_month,                            #6  -- TODO more
                                'invoiceEndDate': datetime.date.today(),                    #7  -- TODO more
                                'providerInvoiceId': _providerInvoiceId,                    #8
                                'providerFinalBillFlag': "" ,                               #9   -- TODO more
                                'providerName': _providerNm,                                #10
                                'assetAccountId': row["accountId"],                         #11
                                'billingAccountId':row["accountId"],                        #12
                                'providerRegion':row["resourceLocation"],                   #13
                                'assetName':get_asset_name(row["instanceId"]),              #14
                                'providerAssetId':row["instanceId"],                        #15
                                'description': "",                                          #16
                                'quantity': row["consumedQuantity"],                        #17
                                'unitOfMeasure': row["unitOfMeasure"],                      #18
                                'providerCurrency': currency_json_resp["currencyCode"],     #19
                                'pcProviderUnitCost': row["resourceRate"],                  #20
                                'pcProviderTotalCost': row["cost"],                         #21
                                'pcProviderTaxCost': _pcProviderTaxCost,                    #22 # Referred from AWS
                                'pcCustomerUnitCost': row["resourceRate"],                  #23
                                'pcCustomerTotalCost': row["cost"],                         #24
                                'customerCurrency': currency_json_resp["currencyCode"],     #25
                                'customerConversionRate': _customerConversionRate,          #26
                                'customerCurrencyDate': "",                                 #27 # Todo more
                                'orderId': ""  ,                                            #28
                                'providerServiceName': row["consumedService"],              #29
                                'providerServiceDescription': "",                           #30
                                'tags': row["tags"]                                         #31
                })


    csv_zipfile_name = 'C_' + filename1 + '1111111'
    csv_zipfile_name = zipfile.ZipFile(csv_zipfile_name + '.zip', 'w')
    with  csv_zipfile_name as myzip:
        for file in . :
            if file.endswith('.csv'):



def get_asset_name(instance_id):
    return instance_id.rpartition('/')[-1]

if __name__ == "__main__":
    parse_response_to_gpd()