
'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get filename
while True:
    fname = raw_input('Enter file name: ');
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break

# get file content (text) lines
alldata = []
print("\nEnter lines ('.' by iteself to quit),\n")

#loop util user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        alldata.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in alldata])
fobj.close()
print('DONE!')
        