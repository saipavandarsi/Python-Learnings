import sys, os
import boto

AWS_ACCESS_KEY_ID = 'AKIAJFGWRIYHNLBUEY3Q'
AWS_SECRET_ACCESS_KEY = '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'

LOCAL_PATH = '/Users/shrmadis/Desktop/personal/Python/Boto/'
bucket_name = 'pythontraining123'

def aws():
    """ 
        boto is used to connect to aws , and S3 service and get the objects 
        from the s3 into the LOACAL_PATH place whatever we mention
    """
    conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(bucket_name)
    bucket_list = bucket.list()
    for l in bucket_list:
        keystring = str(l.key)
        if not os.path.exists(LOCAL_PATH + keystring):
            l.get_contents_to_filename(LOCAL_PATH + keystring)



aws()