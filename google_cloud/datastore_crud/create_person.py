# https://cloud.google.com/datastore/docs/datastore-api-tutorial
# https://googleapis.dev/python/datastore/latest/client.html

from google.cloud import datastore
import datetime
import sys

def create_client(project_id):
    return datastore.Client(project_id)


def create(client, f_name, l_name, age, email_address, nationality, profession):
    key = client.key('Person')
    obj = datastore.Entity(key)

    obj.update({ 
	'created': datetime.datetime.utcnow(), # auto-generated default value
	'first name': f_name, 
	'last name': l_name, 
	'age': age, 
	'contact': email_address, 
	'nationality': nationality,
	'career': profession,
	'status': 'Active'  # setting a default value 
	})
    
    client.put(obj) # insert object into the datastore

    return obj.key


project_id = 'my_project_id_goes_here'
ds_client = create_client(project_id)
create(ds_client, 'Oluremi', 'Tinubu', 23, 'tinubu@azingo.com', 'Togo', 'Accountant')
create(ds_client, 'Solomon', 'Lar', 44, 'solomon.lar@pdp.com', 'Sri Lanka', 'Lawyer')
create(ds_client, 'Hassan', 'Imam', 31, 'hassan@gmail.com', 'Sudan', 'Student')
create(ds_client, 'Mufundu', 'Zuma', 27, 'm.zuma@uwc.com', 'South Africa', 'System Engineer')
create(ds_client, 'Donald', 'Trump', 63, 'donald.trump@abc.com', 'USA', 'Politiciam')
create(ds_client, 'Alfred', 'Cokcs', 23, 'tinubu@azingo.com', 'Australia', 'Chef')
create(ds_client, 'Sogo', 'Dada', 23, 'tinubu@azingo.com', 'Nigeria', 'Project Manager')



