import facebook

# graph = facebook.GraphAPI(access_token='EAACsGdRSUbYBADcpAUDODYeCkClvtz8tVePU8YpyZCCZASXZA8fpBvvxrQ4lXpcxCqsrgPQaAyj35stRa30HRL61OuAu4TWVceIxZBLotMIyYEuX6pl54MhhLpqA7obik3BOA7GrCBou69cpUT817O5ijUkairhOYkIGb0OiK8NOlePyTgsfsL3PHDRPc3wvGljt2lCOVnIkJy6edAAC5VTd1CDe3sJkZAiR7pkUCTQZDZD', version="3.0")
#
# graph.put_object(
#   parent_object=104933378315104,
#   connection_name="Andrew Bryan",
#   message='I just posted automatically with python!',
# )

# import facebook
# print('Facebook Version :', facebook.__version__)
# print('App Version : 1.0')
# other = "EAACsGdRSUbYBADcpAUDODYeCkClvtz8tVePU8YpyZCCZASXZA8fpBvvxrQ4lXpcxCqsrgPQaAyj35stRa30HRL61OuAu4TWVceIxZBLotMIyYEuX6pl54MhhLpqA7obik3BOA7GrCBou69cpUT817O5ijUkairhOYkIGb0OiK8NOlePyTgsfsL3PHDRPc3wvGljt2lCOVnIkJy6edAAC5VTd1CDe3sJkZAiR7pkUCTQZDZD"
# test_user_access_token = "EAACsGdRSUbYBAGZB4ajC9gMle1xrCODM0eQaDhDWzUbA610fq7Ow99N33V60HZBQeK2jranM7KpsGsFu1KEJGNi5FjEJ4LaVNnP0UbjetdKAialL2qkJRHf0Qhz5CNrw0XC2mBW5BCZAZB3ndPZCZBsQsLyPbOlyZALzvJIHr7Fr15wUEFYLgIF2aI4evBXINZBoEq7fFmnZBqwZDZD"
# graph = facebook.GraphAPI(access_token=test_user_access_token)
# page_id_test = "104933378315104"
# message = "please work I beg"

#
# # Need :
# # - Parent_object : page id
# # - connection_name : the wall of the page
# # - message : the message you want to send
# graph.put_object(parent_object=page_id_test, connection_name="Test",
# message=message)
# # No need to put the page id, the access token has it inside ?
# # graph.put_photo(image=open('img.png', 'rb'), message=message)
# print('POST SENT')

import logging
import requests

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)

app_id = "189226936324534"
app_secret = "0c88a482facff495dd5981ce354cce9e"
user_short_token = "242451790843115"

url = "https://graph.facebook.com/oauth/access_token"

payload = {
    "grant_type": "fb_exchange_token",
    "client_id": app_id,
    "client_secret": app_secret,
    "fb_exchange_token": user_short_token,
}

try:
    response = requests.get(
        url,
        params=payload,
        timeout=5,
    )

except requests.exceptions.Timeout as e:
    logging.error("TimeoutError", e)

else:

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error("HTTPError", e)

    else:
        response_json = response.json()
        logging.info(response_json)
        user_long_token = response_json["access_token"]

"""
print(response_json)
{'access_token': 'EAAPxxxx', 'token_type': 'bearer', 'expires_in': 5183614}
"""