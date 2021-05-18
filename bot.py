from instaclient import InstaClient
from instaclient.errors.common import *
import time

# create the client object
client = InstaClient(driver_path='./chromedriver')
# client = InstaClient(driver=InstaClient.CHROMEDRIVER)

# log in with your Instagram credentials

instaUsername = input('Enter an instagram account\'s username to scrape with: ')
instaPass = input('Enter an instagram account\'s username to scrape with: ')

try:
  client.login(username=instaUsername, password=instaPass)
except SecurityCodeRequired:
  # In case you have 2FA turned on in your IG account
  # Check for the security code in your Authenticator App or via SMS
  code = input('Enter your 2FA security code here: ')
  client.input_security_code(code)


with open('usernames.txt', 'r') as f:
    reference = f.readlines()[-1]

# Scrape Instagram followers
username = input('Enter an instagram account\'s username to scrape it\'s followers: ')

try:
  file = open("usernames.txt", "a")

  if len(reference) < 5:
    reference=None

  # This will try to get the user's first 100 followers 
  while True:
    result = client.get_followers(user=username, count=500, callback_frequency=50, end_cursor=reference)
    reference = result[1]

    for u in result[0]:
        file.write("{},\n".format(u.username))

    file.write("{}\n".format(reference))

    print('Finished writting to file')

    if len(result[0]) < 500:
        break

    time.sleep(100)

  file.close()
  print('finish')
except InvalidUserError:
  # Exception raised if the username is not valid
  print('The username is not valid')
except PrivateAccountError:
  # Exception raised if the account you are trying to scrape is private
  print('{} is a private account'.format(username))