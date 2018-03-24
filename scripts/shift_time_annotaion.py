
# coding: utf-8

# In[21]:

from csv import reader, writer
from tempfile import NamedTemporaryFile
import shutil
import sys
import os

if len(sys.argv) != 3:
    sys.exit('Syntax: command <URI.annotations> <time_to_shift>')


# start_ts, end_ts = load_excerpt(uri_excerpt)
start_ts = float(sys.argv[2])
URI_annotation = sys.argv[1]

fout = NamedTemporaryFile(delete=False)

with open(URI_annotation,'rb') as fin, fout:
    w = writer(fout, delimiter='\t')

    reader = reader(fin, delimiter='\t')
    rows = [r for r in reader]
    
    for row in rows:
            row[0]= float(row[0]) + start_ts
            w.writerow(row)
# rename to original file name or to another name
URI_target = URI_annotation
shutil.move(fout.name, URI_target)            
print 'written file ' + URI_target




