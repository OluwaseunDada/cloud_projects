import boto3, sys

REGION_NAME = 'the-region-name' 
s3_client = boto3.resource('s3', region_name=REGION_NAME)
BUCKET = "the-s3-bucket-name"
PATH = "the-actual-folder-destination/"
FILE_TO_BE_UPLOADED = sys.argv[1]
     
try:
   s3_client.Bucket(BUCKET).upload_file(FILE_TO_BE_UPLOADED, PATH)
   print(FILE_TO_BE_UPLOADED + " has been successfully uploaded to amazon S3 destination : " + BUCKET + "/" + PATH)
except Exception as e:
   print("" + str(e))
   print("ERROR: unable to upload " + FILE_TO_BE_UPLOADED +  " to s3 bucket")

