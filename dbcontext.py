

import httplib2
import Entities.invertor
import Entities.battery
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class DbContext:
    def __init__(self, feeds, drive, cred_path):
        self.scope = [feeds, drive]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, self.scope).authorize(httplib2.Http())
        self.service = build('sheets', 'v4', http=self.creds)
        pass

    def get_all_invertors(self):
        invertorsData = self.service.spreadsheets().values().get(spreadsheetId="1B65wi55wfiTAPCzx21PqQG9bjBetZKy11j417R1ZUZU", range="Invertors!A2:E3").execute()
        invertors = [Entities.invertor.Invertor(item[0], item[1], item[2], item[3]) for item in invertorsData.get('values', [])]
        return invertors
    
    def get_all_batteries(self):
        batteriesData = self.service.spreadsheets().values().get(spreadsheetId="1B65wi55wfiTAPCzx21PqQG9bjBetZKy11j417R1ZUZU", range="Batteries!A2:E3").execute()
        batteries = [Entities.battery.Battery(item[0], item[1], item[2], item[3]) for item in batteriesData.get('values', [])]
        for bat in batteries:
            print(bat.json_serialize())
        return batteries