from instaclient import InstaClient
from instaclient.errors.common import *
import time

# create the client object
client = InstaClient(driver_path='./chromedriver')
# client = InstaClient(driver=InstaClient.CHROMEDRIVER)

instaUsername = input('Enter an instagram account\'s username to scrape with: ')
instaPass = input('Enter an instagram account\'s password to scrape with: ')

# log in with your Instagram credentials
try:
  client.login(username=instaUsername, password=instaPass)
except SecurityCodeRequired:
  # In case you have 2FA turned on in your IG account
  # Check for the security code in your Authenticator App or via SMS
  code = input('Enter your 2FA security code here: ')
  client.input_security_code(code)

# Scrape Instagram followers
# username = input('Enter an instagram account\'s username to scrape it\'s followers: ')

with open('usernames.csv', 'r') as f:
    usernames = f.readlines()

for username in usernames: 
    time.sleep(1)
    profile = client.get_profile(username, True)
    print("{}={}".format(username.rstrip(), profile.business_email))


