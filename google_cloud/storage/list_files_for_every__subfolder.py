
import sys
from google.cloud import storage


def list_per_subdir(bucket, subfolder_name):
   blobs = list(bucket.list_blobs(prefix=subfolder_name)) # sys.argv[2] == subfolder_name
   
   if subfolder_name == None:
       print("\n###### below are the contents of the " +  bucket.name + " bucket:\n")
   else:
       print("\n###### below are the contents of the sub-folder gs://" + bucket.name + "/" +  subfolder_name  + " \n")
   for b in blobs:
     print (b.name)


def main():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(sys.argv[1]) # sys.argv[1] == bucket_name
    subfolder_name = None

    if len(sys.argv) < 3:
       subfolder_name = None   # empty == subfolder_name
    else:
       subfolder_name = sys.argv[2] 
       # the + '/' ensures that only the actual contents of the subfolder are listed
       if sys.argv[2].endswith('/'):
            subfolder_name = sys.argv[2]
       else:
            subfolder_name = sys.argv[2] + '/'

    # list
    list_per_subdir(bucket, subfolder_name)


# usage example:
# python app_name.py bucket_name
    # if no extra argument is provided, it lists all contents in the bucket
# python app_name.py bucket_name subfolder_name
    # it lists the contents in the specified subfolder
main()
