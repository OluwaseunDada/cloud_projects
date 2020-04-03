
import sys
from google.cloud import storage
import googleapiclient.discovery

def list_per_subdir(bucket, subfolder_name):
   blobs = list(bucket.list_blobs(prefix=subfolder_name)) # sys.argv[2] == subfolder_name
   
   if subfolder_name == None:
       print("\n###### below are the contents of the " +  bucket.name + " bucket:\n")
   else:
       print("\n###### below are the contents of the sub-folder gs://" + bucket.name + "/" +  subfolder_name  + " \n")
   for b in blobs:
     print (b.name)



def list_sub_directories(bucket_name, prefix):
    """Returns a list of sub-directories within the given bucket."""
    service = googleapiclient.discovery.build('storage', 'v1')
    req = service.objects().list(bucket=bucket_name, prefix=prefix, delimiter='/')
    res = req.execute()
    return res['prefixes']


def main():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(sys.argv[1]) # sys.argv[1] == bucket_name

    sub_folder_list = list_sub_directories(bucket_name=sys.argv[1], prefix=None)
    print(sub_folder_list)
    
    # loop the available subfolders
    for folder in sub_folder_list:
       list_per_subdir(bucket, folder)


# usage example:
# python app_name.py bucket_name
    # if no extra argument is provided, it lists all contents in the bucket
# python app_name.py bucket_name subfolder_name
    # it lists the contents in the specified subfolder
main()
