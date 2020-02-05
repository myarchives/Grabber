import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Grabber').sheet1

stuffs = sheet.get_all_records()
print(stuffs)
