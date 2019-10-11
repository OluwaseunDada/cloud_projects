# https://cloud.google.com/datastore/docs/datastore-api-tutorial
# https://googleapis.dev/python/datastore/latest/client.html

from google.cloud import datastore
import datetime
import sys

def create_client(project_id):
    return datastore.Client(project_id)


def delete_person(client, person_id):
    key = client.key('Person', person_id)
    client.delete(key)



project_id = 'my_project_id_goes_here'
ds_client = create_client(project_id)


person_id = 294 # this is chef's id in the datastore
delete_person(ds_client, person_id)

print("deletion successful!")


