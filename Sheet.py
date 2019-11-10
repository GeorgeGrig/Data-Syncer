import gspread
import os
import time
import Logs
import subprocess
import sys
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
MainProgram = 'WhateverTheMainProgramIsNamed.exe'

def DataFetcher() :
    try:
        sheet = client.open("Properties").sheet1 #which already shared google sheet to access 
        LAST = sheet.cell(1, 2).value
        HASHTAG_POS = sheet.cell(2, 2).value
        HASHTAG = sheet.cell(3, 2).value
        sheet1 = client.open("Hidden").sheet1 
        SWITCH_POS = sheet1.cell(1, 2).value
        Latest_Version = float(sheet1.cell(2, 2).value)
        Update_Link = sheet1.cell(3, 2).value
    except:
        Logs.print2('**FAILED** to load data from sheets')
        time.sleep(10)
        sys.exit(0)
    return [LAST,HASHTAG,HASHTAG_POS,SWITCH_POS,Latest_Version,Update_Link]

def DataEditor(LAST,HASHTAG_POS,HASHTAG):
    try:
        sheet = client.open("Properties").sheet1 #which already shared google sheet to access 
        LAST_OLD = sheet.cell(1, 2).value
        if int(HASHTAG) > int(LAST_OLD):
            HASHTAG = HASHTAG.replace("HASHTAG=", "")
            LAST = LAST.replace("LAST=", "")
            HASHTAG_POS = HASHTAG_POS.replace("HASHTAG_POS=", "")
            sheet.update_cell(3, 2, str(LAST))
            sheet.update_cell(2, 2, str(HASHTAG_POS))
            sheet.update_cell(1, 2, str(HASHTAG))
        else:
            Logs.print2('No changes detected')
    except:
        Logs.print2('**FAILED** to write data to sheets')
        time.sleep(10)
        sys.exit(0) 

def DataLogger(user_name,unique_hw_id,WORK_DONE): 
    sheet = client.open("LOGS").sheet1
    USER_FINDER = sheet.cell(3, 2).value
    i=2 
    while USER_FINDER != "":                                                       #searches if user already exists
        if USER_FINDER == str(user_name)+str(unique_hw_id):
            break
        i = i+1
        USER_FINDER = sheet.cell(3, i).value
    
    if USER_FINDER == "":                                                          #if he doesn't exist , creates new entry
       sheet.update_cell(3, i, str(user_name)+str(unique_hw_id) )
    OLD_WORK = sheet.cell(2, i).value                                              
    sheet.update_cell(2, i, int(OLD_WORK) + int(WORK_DONE))                         #ADDS WORK DONE TO TOTAL
    j=4 
    EMPTY_LOG_FINDER = sheet.cell(4, i).value                                       #finds empty log cell
    while  EMPTY_LOG_FINDER != "":
        j= j+1
        EMPTY_LOG_FINDER = sheet.cell(j, i).value
    current = time.ctime(), WORK_DONE
    sheet.update_cell(j, i, str(current) )   

def MainProgramCall():
    sheet1 = client.open("Hidden").sheet1 
    sheet1.update_cell(1, 2, 'ON')
    p = subprocess.call(['java', '-jar', MainProgram],shell=True) # START Main Program,mine was a java application 

def Exit(p):                                                                  #shutdown admin edit script                        
    sheet1 = client.open("Hidden").sheet1 
    sheet1.update_cell(1, 2, 'OFF')
    p.terminate() 
