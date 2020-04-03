

import googleapiclient.discovery
import sys



def list_sub_directories(bucket_name, prefix):
    """Returns a list of sub-directories within the given bucket."""
    service = googleapiclient.discovery.build('storage', 'v1')

    req = service.objects().list(bucket=bucket_name, prefix=prefix, delimiter='/')
    res = req.execute()
    return res['prefixes']

aList = list_sub_directories(bucket_name=sys.argv[1], prefix=None)
print(aList)

