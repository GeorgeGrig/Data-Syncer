# Data-Syncer
Syncs local values of a file using Google Sheets as a free, always online "database".

## Disclaimer
This might or might not work for you, I really don't plan to maintain it at all.
## Prerequisites
In order to run the script you need to have the following:
```
gspread ---> https://github.com/burnash/gspread/
oauth2client
```
## Getting started
* Put a working client_secret.json for Google sheets access inside the script folder (how-To: https://developers.google.com/sheets/api/quickstart/python)

* Create a google sheet named "Hidden" This will be your remote control center,the first line of the B column is the switch,it's the way for the script to check whether another instance is running or it shut down incorrectly (Also,if you set it to "BLOCK" you can block the program from running),the second line is the version number,setting to it to a higher number will force the users to update using the link provided in the third line of column B.

* Create a google sheet named "Properties" This will store the values that are synced between devices.

* Create a google sheet named "LOGS" This will store the any log info,including a unique identifier for each computer,a total differnce for one of the variables and a total for each user,this function might not be especially useful for you,exclude it if needed.

* Give access to your developer account.

## Known issues
None,other than sometimes the script might not shutdown correctly and it might fail to sync (you will know because the Hidden value will be left to ON).
