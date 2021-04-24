"""This is a Test Program to understand the functionality of google maps
using
    -api key
    -getting  query
    -understanding how to implement for future automation

    - needed criteria for place serch for http requests
        -location (long, lat)
        -radius (distance from center)
        -type (name)
        -name (unknown)

        https://maps.googleapis.com/maps/api/place/nearbysearch/json
        ?location=-33.8670522,151.1957362
        &radius=500
        &types=food
        &name=harbour



"""
import requests, json
import pandas as pd
import openpyxl

# enter your api key here
api_key = 'AIzaSyAXU1TdAhdKicccFRET4DIdOEV_KifBx7o'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
queryType = input('Search queryType: ')
cityName = input('Search City: ')
stateName = input('Search State: ')

queryType = queryType + ' ' + cityName + ' ' + stateName

# get method of requests module
# return response object
r = requests.get(url + 'query=' + queryType + '&feilds=name/formatted_address' +
                 '&key=' + api_key )

# json method of response object convert
#  json format data into python format data
x = r.json()
#print(x)

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']
nextpage = x['next_page_token']

#print(nextpage)

#print(y)

# keep looping upto length of y
#for i in range(len(y)):
    # Print value corresponding to the
    # 'name' key at the ith index of y
#    print(y[i]['name'])
#    print(y[i]['formatted_address'])

#to xlsx
#pd.DataFrame(y).to_excel(queryType+cityName+'.xlsx')
df = pd.DataFrame(y)

df.drop(['business_status','geometry','icon','opening_hours','photos','plus_code','user_ratings_total'], axis=1, inplace=True)
#print(df.head())
#df = pd.read_json(y)

for index ,place in df.iterrows():
    print(place['name'])

#df.to_excel(queryType+cityName+'.xlsx')

