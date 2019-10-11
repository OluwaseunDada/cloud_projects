# https://cloud.google.com/datastore/docs/datastore-api-tutorial
# https://googleapis.dev/python/datastore/latest/client.html

from google.cloud import datastore
import datetime
import sys

def create_client(project_id):
    return datastore.Client(project_id)


def update(client, person_id, new_email, new_nationality):
    with client.transaction():
        key = client.key('Person', person_id)
        obj = client.get(key)

        if not obj:
            raise ValueError(
	        # raise exception if the person is not found in the datastore
                'person {} does not exist.'.format(person_id))

	# update existing values		
        obj['contact'] = new_email
        obj['nationality'] = new_nationality

        client.put(obj) # save changes 


project_id = 'my_project_id_goes_here'
person_id = 292 # this is the ID for Mufundu Zuma
update(ds_client, 292, 'mufundu.z@uct.com', 'Zimbabwe')



