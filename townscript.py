import requests

url = "https://www.townscript.com/api/registration/getRegisteredUsers?eventCode=annyeong-korea-201304"

headers = {
    "accept": "application/json",
    "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJST0xFIjoiUk9MRV9VU0VSIiwic3ViIjoidmVydGV4a29yZWFuZXZlbnRAZ21haWwuY29tIiwiYXVkaWVuY2UiOiJ3ZWIiLCJjcmVhdGVkIjoxNjk5NjQzNzI5NDY1LCJNQUdJQ19MT0dJTiI6ZmFsc2UsIlVTRVJfSUQiOjQ4NzcyODIsImV4cCI6MTcwNzQxOTcyOX0.BTayty_RVNwM4yRnB_2Zf7yIreQ-OAQ2D33mW4hhiqzUzkbmD6W17Xs2Im0ULdSJLVtRISGJTUvI1gVSMBSKsQ"
}

response = requests.get(url, headers=headers)

print(response.json())