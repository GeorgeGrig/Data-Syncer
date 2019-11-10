import sys
import os
file = 'properties' #file to open


def Reader() :

    lines = [] 
    f = open(file,"r+") #open for read/write
    for line in f:lines.append(line)
    lines[2] = lines[2].replace("HASHTAG=", "")
    lines[3] = lines[3].replace("LAST=", "")
    lines[4] = lines[4].replace("HASHTAG_POS=", "")
    date = lines[1]
    hashtag = lines[2]
    last_uploaded = lines[3]
    hash_position = lines[4]
    f.close()
    return [date,hashtag,last_uploaded,hash_position]

def Reader2() :
    lines = [] 
    f = open(file,"r+") #open for read/write
    for line in f:lines.append(line)
    lines[3] = lines[3].replace("HASHTAG=", "")
    lines[2] = lines[2].replace("LAST=", "")
    lines[4] = lines[4].replace("HASHTAG_POS=", "")
    date = lines[1]
    hashtag = lines[3]
    last_uploaded = lines[2]
    hash_position = lines[4]
    f.close()
    return [date,hashtag,last_uploaded,hash_position]

def Editor(DATE,LAST,HASHTAG_POS,HASHTAG):
    try:
        f = open(file,"w")
        f.write('#')
        f.write('\n')
        f.write(str(DATE))
        f.write('HASHTAG=')
        f.write(str(HASHTAG))
        f.write('\n')
        f.write('LAST=')
        f.write(str(LAST))
        f.write('\n')
        f.write('HASHTAG_POS=')
        f.write(str(HASHTAG_POS))
        f.write('\n')
        f.write('DEBUG=TRUE')
        f.close()
    except:
        Logs.print2('**FAILED** to write local properties')
        time.sleep(10)
        sys.exit(0) 

def OrderCorrector():
    lines = [] 
    f = open(file,"r+") #open for read/write
    for line in f:lines.append(line)
    if 'HASHTAG=' in lines[2]: 
        [DATE,LAST_LOCAL,HASHTAG_LOCAL,HASHTAG_POS_LOCAL] = Reader()
    elif "LAST=" in lines[2]:
        [DATE,LAST_LOCAL,HASHTAG_LOCAL,HASHTAG_POS_LOCAL] = Reader2()
    return [DATE,LAST_LOCAL,HASHTAG_LOCAL,HASHTAG_POS_LOCAL]
