import requests
import json
import generator
import time
import re

mail_session = requests.Session()
base_url = "https://api.mail.tm"

# # Get Domain
# domains = requests.get(base_url + "/domains").text
# domain_json = json.loads(domains)
# domain = domain_json['hydra:member'][0]['domain']

# # Create Email Account
# email_address = generator.generate() + "@" + domain

def email(email_address):
    # Create Email Account
    create_email = requests.post(base_url + "/accounts", json={"address": email_address, "password": "123m321M@"})

    # Get Token
    token_address = requests.post(base_url + "/token", json={"address": email_address, "password": "123m321M@"})

    # Set Token In Session
    mail_session.headers = {"Authorization": "Bearer " + json.loads(token_address.text)['token']}

    profile = mail_session.get(base_url + "/me")
    print(profile.text)

    # Waiting For Message
    verify_mail = ""
    keep_going = True
    counter = 0
    while(keep_going):
        if counter >= 10:
            break

        print("Waiting for message...")
        messages = mail_session.get(base_url + "/messages")
        if json.loads(messages.text)['hydra:totalItems'] == 1:
            message = mail_session.get(base_url + "/messages/" + json.loads(messages.text)['hydra:member'][0]['id'])
            verify_mail = json.loads(message.text)['text']
            # keep_going = False
            break
        counter += 1
        time.sleep(2)


    try:
        # Find Link
        verify_search = re.search("https:..netshekan.info.login.php.activate=.*", verify_mail)
        verify_link = verify_search.group()
        # print(verify_link)
        s = requests.get(verify_link)
        # print(s.text)

        return 1
    except:
        return 0