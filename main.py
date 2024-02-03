from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
import requests
import re
import generator
import num_generator
import email_stuff
import json
from bs4 import BeautifulSoup

# # Generate Email First Step
# # Get Domain
# domains = requests.get("https://api.mail.tm/domains").text
# domain_json = json.loads(domains)
# domain = domain_json['hydra:member'][0]['domain']

# # Create Email Account
# email_address = generator.generate() + "@" + domain

# # Captcha Calculate Variables
# first_num = 0
# second_num = 0
# sum_num = 0

# # Session
# session = requests.Session()

# # Register
# response = session.get("https://netshekan.info/register")

# soup = BeautifulSoup(response.text, "html.parser")
# captcha_text = soup.select_one('span[id="captcha"]').string

# first_num = num_generator.calc(captcha_text.split()[0])
# second_num = num_generator.calc(captcha_text.split()[2])
# if captcha_text.split()[1] == "به‌اضافه":
#     sum_num = first_num + second_num

# if captcha_text.split()[1] == "منهای":
#     sum_num = first_num - second_num

# headers_register = {
#     'authority': 'netshekan.info',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'dnt': '1',
#     'origin': 'https://netshekan.info',
#     'referer': 'https://netshekan.info/register',
#     'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
#     'x-requested-with': 'XMLHttpRequest',
# }

# data_register = {
#     'action': 'register',
#     'Name': generator.generate(),
#     'Email': email_address,
#     'Mobile': '09111111111',
#     'UserName': generator.generate(),
#     'Password': '123m321M@',
#     'Captcha': sum_num,
# }

# response = session.post('https://netshekan.info/includes/ajax.php', headers=headers_register, data=data_register)
# print(response.text)
# if response.text == "6":
#     print("Success")

# # Verify Email
# status = email_stuff.email(email_address)

# if (status):
#     # Login
#     response = session.get("https://netshekan.info/login")

#     soup = BeautifulSoup(response.text, "html.parser")
#     captcha_text = soup.select_one('span[id="captcha"]').string

#     first_num = num_generator.calc(captcha_text.split()[0])
#     second_num = num_generator.calc(captcha_text.split()[2])
#     if captcha_text.split()[1] == "به‌اضافه":
#         sum_num = first_num + second_num

#     if captcha_text.split()[1] == "منهای":
#         sum_num = first_num - second_num


#     headers_login = {
#         'authority': 'netshekan.info',
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'dnt': '1',
#         'origin': 'https://netshekan.info',
#         'referer': 'https://netshekan.info/login',
#         'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
#         'x-requested-with': 'XMLHttpRequest',
#     }

#     data_login = {
#         'action': 'login',
#         'UserName': email_address,
#         'Password': '123m321M@',
#         'Captcha': sum_num,
#     }

#     response = session.post('https://netshekan.info/includes/ajax.php', headers=headers_login, data=data_login)


#     # Getting V2ray Link
#     session.get("https://netshekan.info/cart/?add=1")
#     config_page = session.get("https://netshekan.info/download/")
#     vpn_link = re.search("vless:.*🇩🇪", config_page.text)
#     print(vpn_link.group())
# else:
#     print("Failed stop")


# ---------------------------------------------------------------------
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/config", response_class=PlainTextResponse)
def test_route():
    # Generate Email First Step
    # Get Domain
    domains = requests.get("https://api.mail.tm/domains").text
    domain_json = json.loads(domains)
    domain = domain_json['hydra:member'][0]['domain']

    # Create Email Account
    email_address = generator.generate() + "@" + domain

    # Captcha Calculate Variables
    first_num = 0
    second_num = 0
    sum_num = 0

    # Session
    session = requests.Session()

    # Register
    response = session.get("https://netshekan.info/register")

    soup = BeautifulSoup(response.text, "html.parser")
    captcha_text = soup.select_one('span[id="captcha"]').string

    first_num = num_generator.calc(captcha_text.split()[0])
    second_num = num_generator.calc(captcha_text.split()[2])
    if captcha_text.split()[1] == "به‌اضافه":
        sum_num = first_num + second_num

    if captcha_text.split()[1] == "منهای":
        sum_num = first_num - second_num

    headers_register = {
        'authority': 'netshekan.info',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://netshekan.info',
        'referer': 'https://netshekan.info/register',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    data_register = {
        'action': 'register',
        'Name': generator.generate(),
        'Email': email_address,
        'Mobile': '09111111111',
        'UserName': generator.generate(),
        'Password': '123m321M@',
        'Captcha': sum_num,
    }

    response = session.post('https://netshekan.info/includes/ajax.php', headers=headers_register, data=data_register)
    print(response.text)
    if response.text == "6":
        print("Success")

    # Verify Email
    status = email_stuff.email(email_address)

    if (status):
        # Login
        response = session.get("https://netshekan.info/login")

        soup = BeautifulSoup(response.text, "html.parser")
        captcha_text = soup.select_one('span[id="captcha"]').string

        first_num = num_generator.calc(captcha_text.split()[0])
        second_num = num_generator.calc(captcha_text.split()[2])
        if captcha_text.split()[1] == "به‌اضافه":
            sum_num = first_num + second_num

        if captcha_text.split()[1] == "منهای":
            sum_num = first_num - second_num


        headers_login = {
            'authority': 'netshekan.info',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://netshekan.info',
            'referer': 'https://netshekan.info/login',
            'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        data_login = {
            'action': 'login',
            'UserName': email_address,
            'Password': '123m321M@',
            'Captcha': sum_num,
        }

        response = session.post('https://netshekan.info/includes/ajax.php', headers=headers_login, data=data_login)


        # Getting V2ray Link
        session.get("https://netshekan.info/cart/?add=1")
        config_page = session.get("https://netshekan.info/download/")
        vpn_link = re.search("vless:.*🇩🇪", config_page.text)
        return vpn_link.group()
    else:
        print("Failed stop")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)