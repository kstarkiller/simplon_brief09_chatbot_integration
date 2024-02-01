# import json
# import requests
import my_bot

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA5ZTFhOTMtMjZhYi00NTY3LTliODItZDk2NTk4YmNhODIyIiwidHlwZSI6ImFwaV90b2tlbiJ9.IP0_jpdfxZPAhu6R7bT64EPEXNWz2uml2YX6nzSY61I"}

provider = "meta"

url = "https://api.edenai.run/v2/text/chat"

my_bot.bot_request(provider, url, headers)