import boto3, sys
import subprocess, os

FILE_TO_BE_UPLOADED = sys.argv[1]
destination = sys.argv[2]
destination_parts = destination.split('/', 1)
BUCKET = destination_parts[0]
PATH = destination_parts[1]
aws_region_name = 'some_aws_region_name'

def release_to_gcp_bucket():
    # gsutil cp -c -L $(basename ${file}).log -r ${file} ${destination}		
    result = subprocess.Popen(['gsutil', 'cp', '-c', '-L', 'output.log', '-r',  FILE_TO_BE_UPLOADED, destination], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = result.communicate()
   
    for line in open("output.log", "r").readlines(): print(line)
    os.remove("output.log")

def upload_file_s3_bucket():     
  try:
     s3_client = boto3.resource('s3', region_name=aws_region_name)
     s3_client.Bucket(BUCKET).upload_file(FILE_TO_BE_UPLOADED, PATH)
     print(FILE_TO_BE_UPLOADED + " has been successfully uploaded to amazon S3 destination : " + BUCKET + "/" + PATH)
  except Exception as e:
     print("" + str(e))
     print("ERROR: unable to upload " + FILE_TO_BE_UPLOADED +  " to s3 bucket")



if 'gs://' in destination:
   # this is google-cloud destination
   release_to_gcp_bucket()

else:
   # amazon s3-bucket
   upload_file_s3_bucket()
