import boto3
import os
import ast
import json
import requests

PET_FINDER_API_ENDPOINT = 'https://api.petfinder.com/v2/'

def getToken():
    AUTH_URL = PET_FINDER_API_ENDPOINT + 'oauth2/token'
    PET_FINDER_API_CLIENT_ID = os.environ.get('PET_FINDER_API_CLIENT_ID')
    PET_FINDER_API_SECRET = os.environ.get('PET_FINDER_API_SECRET')

    post_fields = {'grant_type': 'client_credentials', 
                    'client_id' : PET_FINDER_API_CLIENT_ID,
                    'client_secret' : PET_FINDER_API_SECRET}
    response = requests.post(AUTH_URL,post_fields)

    return ast.literal_eval(response.text)['access_token']

def parseQueueEvent(event):
    body_record = event['Records'][0]['body']
    body_dict = ast.literal_eval(body_record)
    return body_dict

def runQuery(event,context):
    QUERY_URL = PET_FINDER_API_ENDPOINT + 'animals'

    token = getToken()
    auth_header = {'Authorization': 'Bearer ' + token}
    
    #parse out queue JSON with query fields
    query_fields = parseQueueEvent(event)

    #remove and save fields not relevant to the query
    #remaining fields should be part of the query
    email = query_fields.pop('email',None)
    is_test = query_fields.pop('test', None)

    #run the query against PetFinderApi
    #return the results.
    # request = Request(QUERY_URL, data=urlencode(query_fields).encode(), headers=auth_header,method='GET' )
    # response = urlopen(request).read().decode()
    r = requests.get(QUERY_URL,
                     headers=auth_header,
                     params=query_fields)

    return r.text

print(getToken())



    


   