import dbcontext
import os

dbctx = dbcontext.DbContext('https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'conf\\credentials.json')


listInvertors = dbctx.get_all_invertors()
print(listInvertors)