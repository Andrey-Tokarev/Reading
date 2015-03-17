import urllib2
import re
import os
from random import randint

text_length = 2 # length (in paragraphs) of the displayed text
source_file = 'ClassicReader.txt'
if not os.path.isfile(source_file): print "Wrong!"
f = open(source_file, 'r')
lines = f.readlines()
f.close()
book, chapter = lines[randint(0, len(lines) - 1)].split()
root = 'http://www.classicreader.com'
url = root + '/book/' + str(book) + '/' + chapter + '/'
url = "http://www.classicreader.com/book/3703/22/"
url = "http://www.classicreader.com/book/53/53/"
try:
  result = urllib2.urlopen(url)
  html = result.read()
except urllib2.URLError, e:
  print "Wrong"

mo = re.search('<title>(.*)</title>', html, re.S) # title
title = mo.group(1)
pars = re.findall('<p>(.*)</p>', html, re.S)
#pars = pars[0].split('</p>\r?\n\r?\n<p>')
pars = re.split('</p>\s+<p>', pars[0])

n_pars = len(pars)
start_par = randint(0, n_pars - text_length)
end_par = start_par + text_length - 1
for i in xrange(start_par, end_par + 1):
    mo = re.search(r">(.*)<", pars[i])
    p1 = mo.group(1)
    p2 = pars[i][pars[i].find('a>') + 2:]
    print
    print p1 + p2
