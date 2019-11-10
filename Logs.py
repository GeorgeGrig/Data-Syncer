import sys
import os
import time
import subprocess


def print2(text):
    print (text)
    with open("logs", "a",encoding='utf-8') as f:
     f.write(time.ctime()+":"+text+"\n")

def UniqueIdentifier():
    user_name = os.getenv('username')
    unique_hw_id = subprocess.check_output('wmic csproduct get uuid')
    return [user_name,unique_hw_id]     
