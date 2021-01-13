# Data-Syncer
Syncs local values of a file using Google Sheets as a free, always online "database".

## Getting started  
* In order to run the script you need to install all the required prerequisites.
* Put a [working](https://developers.google.com/sheets/api/quickstart/python)  client_secret.json for Google sheets access inside the script folder.  
* Create a google sheet named "Hidden", this will be your remote control center,the first line of the B column is the switch,it's the way for the script to check whether another instance is running or it shut down incorrectly (Also,if you set it to "BLOCK" you can block the program from running),the second line is the version number,setting to it to a higher number will force the users to update using the link provided in the third line of column B.
* Create a google sheet named "Properties", this will store the values that are synced between devices.  
* Create a google sheet named "LOGS" This will store the any log info,including a unique identifier for each computer,a total differnce for one of the variables and a total for each user,this function might not be especially useful for you,exclude it if needed.
* Give sheet access to your developer account.

## Known issues
None,other than sometimes the script might not shutdown correctly and it might fail to sync (you will know because the Hidden value will be left to ON).
