from amazonbot import AmazonBot
import gspread
from notifier import SendMail
from oauth2client.service_account import ServiceAccountCredentials

total = []


class PriceUpdater(object):
    def __init__(self, spreadsheet_name):

        self.item_col = 1
        self.name_col = 2
        self.url_col = 3
        self.price_col = 4
        self.total_col = 7

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            '/home/hakanohi/Projects/Grabber/Engine/secret.json', scope)

        client = gspread.authorize(creds)

        self.sheet = client.open(spreadsheet_name).sheet1

    def ProcessList(self):
        items = self.sheet.col_values(self.item_col)[1:]

        amazon_bot = AmazonBot(items)
        prices, urls, names = amazon_bot.search_items()

        print('Updating spreadsheet!')
        for i in range(len(prices)):
            self.sheet.update_cell(i+2, self.name_col, names[i])
            self.sheet.update_cell(i+2, self.url_col, urls[i])
            self.sheet.update_cell(i+2, self.price_col, prices[i])
        total = self.sheet.col_values(self.total_col)[1]
        print(f'Total: {total}')
        return total

def scraperEvent():
    updater = PriceUpdater('Grabber')
    total.append(updater.ProcessList())
    print(total[0])
    SendMail(1, total)
