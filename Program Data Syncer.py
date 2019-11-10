import subprocess
import os
import datetime
import webbrowser
import sys
import time
import unicodedata
import LocalProperties
import Sheet
import Logs
Current_Version = float("1.3")
script = 'NameOfTheScript.exe'



def main (LAST,HASHTAG,HASHTAG_POS,SWITCH_POS_SHEETS):
     [DATE,LAST_LOCAL,HASHTAG_POS_LOCAL,HASHTAG_LOCAL] = LocalProperties.Reader()
     LocalProperties.Editor(DATE,LAST,HASHTAG_POS,HASHTAG)                            #sets local properties file to sheets values
     choice = input("Wanna run the additional script? [Y] OR [N]: ")
     if choice == "N" or choice == "n" or choice == "ν" or choice == "Ν":
         Logs.print2("Cool")
     elif choice == "Y" or choice == "y" or choice == "υ" or choice == "Υ":
         Logs.print2("Cool Cool")
         p = subprocess.Popen([script])                            #RUNS ADMIN EDIT SCRIPT
     Logs.print2("Starting main program...")
     Sheet.MainProgramCall()                                                                  #starts program and sets sheets to ON
     Logs.print2("Seems like the program has been terminated")
     Logs.print2("Setting global values to Google sheets and adding log entries") 
     [DATE,LAST_LOCAL,HASHTAG_LOCAL,HASHTAG_POS_LOCAL] = LocalProperties.OrderCorrector()            #reads changed local properties AND corrects case
     #VALUE CORRECTION
     LAST_LOCAL = LAST_LOCAL.replace("LAST=", "")
     LAST_LOCAL = LAST_LOCAL.replace("/n", "")
     WORK_DONE = int(HASHTAG_LOCAL) - int(LAST)
     #VALUE CORRECTION
     [user_name,unique_hw_id] = Logs.UniqueIdentifier()                                   #gets unique ids to local vars
     Sheet.DataLogger(user_name,unique_hw_id,WORK_DONE)                                    #logs them
     Sheet.DataEditor(LAST_LOCAL,HASHTAG_POS_LOCAL,HASHTAG_LOCAL)                     #sets values to sheets
     try:
         Sheet.Exit(p)
     except:
         print("Could terminate script or it wasn't initiated")

     
def handler():
    with open("logs", "a",encoding='utf-8') as f:
        f.write("###########################"+"\n")
    Logs.print2("Fetching Data")
    [LAST,HASHTAG,HASHTAG_POS,SWITCH_POS_SHEETS,Latest_Version,Update_Link] = Sheet.DataFetcher()
    if Latest_Version > Current_Version:
        Logs.print2 ("Seems like you are not running the latest version of this awesome program,\n current version is: "+str(Current_Version)+" and the latest version is: "+str(Latest_Version))
        choice = input("Do you wish to update? [Y] OR [N]: ")
        if choice == "N" or choice == "n" or choice == "ν" or choice == "Ν":
            sys.exit(0)
        elif choice == "Y" or choice == "y" or choice == "υ" or choice == "Υ":
          Logs.print2("Update link is: "+Update_Link)
          webbrowser.open_new(Update_Link)
    else:
        if SWITCH_POS_SHEETS == "BLOCK":
            sys.exit(0)
        elif SWITCH_POS_SHEETS == "ON":
            choice = input("Program is already running somewhere,continue anyway? [Y] OR [N] (Might lead to sync coflicts): ")
            if choice == "N" or choice == "n" or choice == "ν" or choice == "Ν":
                sys.exit(0)
            elif choice == "Y" or choice == "y" or choice == "υ" or choice == "Υ":
              Logs.print2("Proceeding....")
              main(LAST,HASHTAG,HASHTAG_POS,SWITCH_POS_SHEETS)          
        elif SWITCH_POS_SHEETS == "OFF":
            Logs.print2("Proceeding")
            main(LAST,HASHTAG,HASHTAG_POS,SWITCH_POS_SHEETS)  
handler() 
time.sleep(5)
Logs.print2("Done")
