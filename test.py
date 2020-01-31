import requests

SPACE = "---------------------------------------------------------------------------------------------------------------"
# https://api.telegram.org/bot<token>/getUpdates
TOKEN = '1040218815:AAF4u8NO6K9MZ5LdqSI-lXLV3P4atRUEFsE'
# https://api.telegram.org/bot1040218815:AAF4u8NO6K9MZ5LdqSI-lXLV3P4atRUEFsE/getUpdates
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

r = requests.get(f'{MAIN_URL}/getUpdates')

f = open("text.json", "a")
f.write(f"\n\n{SPACE}\n\n" + str(r.json()))
