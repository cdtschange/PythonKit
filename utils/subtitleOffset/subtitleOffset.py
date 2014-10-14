#coding=utf-8
import re
import os

# get filename
fname = raw_input('Enter filename: ')
foffsetsec = raw_input('Enter offset sec: ')

# fname = r'/Users/cdts_work/Downloads/262397.Coherence_2013_1080p_BluRay_x264_YIFY/Coherence.2013.1080p.BluRay.x264.YIFY.srt'
# foffsetsec = -3

def offset_repl(matchobj):
    oldsec = matchobj.group(2)
    old = int(oldsec)
    sec = old+int(foffsetsec);
    sec = sec if sec>0 else 0
    newsec = "%02d" % sec
    newstr = matchobj.group(1)+newsec+matchobj.group(3)
    return newstr

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:",e)
else:
    # display contents to the Screen
    ff = open ( os.path.split(fname)[0]+'/result.txt', 'w' )  
    for eachLine in fobj:
        egex=ur"(\d+:\d+:)(\d+)(,\d+)" #正则表达式
        newline = re.sub(egex, offset_repl, eachLine)
        ff.write ( newline ) 
        print newline
    
    fobj.close() 
    ff.close()  

print 'finished'
