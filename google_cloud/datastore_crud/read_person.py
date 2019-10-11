# https://cloud.google.com/datastore/docs/datastore-api-tutorial
# https://googleapis.dev/python/datastore/latest/client.html

from google.cloud import datastore
import datetime
import sys

def create_client(project_id):
    return datastore.Client(project_id)



# this function reads and returns the list of all persons in the datastore
def list_all_persons(client):
    query = client.query(kind='Person')
    query.order = ['created']

    return list(query.fetch())


project_id = 'my_project_id_goes_here'
ds_client = create_client(project_id)

list = list_all_persons(ds_client)

for person in list:
   print(person)


