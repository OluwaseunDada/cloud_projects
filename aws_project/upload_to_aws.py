import boto3, sys


FILE_TO_BE_UPLOADED = sys.argv[1]
destination = sys.argv[2]
destination_parts = destination.split('/', 1)
BUCKET = destination_parts[0]
PATH = destination_parts[1]
region_name = 'some-aws-region-name'
     
try:
   s3_client = boto3.resource('s3', region_name=region_name)
   s3_client.Bucket(BUCKET).upload_file(FILE_TO_BE_UPLOADED, PATH)
   print(FILE_TO_BE_UPLOADED + " has been successfully uploaded to amazon S3 destination : " + BUCKET + "/" + PATH)
except Exception as e:
   print("" + str(e))
   print("ERROR: unable to upload " + FILE_TO_BE_UPLOADED +  " to s3 bucket")

