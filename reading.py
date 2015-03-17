import webapp2
import urllib2
import re
import os
from random import randint
# -*- coding: utf-8 -*-
# what's new in the 0.3 version:
# now it deals with English texts from http://www.classicreader.com/

import re #, httplib2 #, os.path
from random import randint
#from bs4 import BeautifulSoup, SoupStrainer


class MainPage(webapp2.RequestHandler):
    def get(self):
      text_length = 2 # length (in paragraphs) of the displayed text
      source_file = 'ClassicReader.txt'
      if not os.path.isfile(source_file): return
      f = open(source_file, 'r')
      lines = f.readlines()
      f.close()
      book, chapter = lines[randint(0, len(lines) - 1)].split()
      root = 'http://www.classicreader.com'
      url = root + '/book/' + str(book) + '/' + chapter + '/'
      self.response.headers['Content-Type'] = 'text/plain'
      #self.response.write(url)
      try:
        result = urllib2.urlopen(url)
        html = result.read()
      except urllib2.URLError, e:
        self.response.write('Something went wrong')
        return
      mo = re.search('<title>(.*)</title>', html, re.S) # title
      title = mo.group(1)
      self.response.write(title)
      pars = re.findall('<p>(.*)</p>', html, re.S)
      pars = re.split('</p>\s+<p>', pars[0])

      n_pars = len(pars)
      start_par = randint(0, n_pars - text_length)
      end_par = start_par + text_length - 1
      for i in xrange(start_par, end_par + 1):
          mo = re.search(r">(.*)<", pars[i])
          p1 = mo.group(1)
          p2 = pars[i][pars[i].find('a>') + 2:]
          self.response.write('\n')
          self.response.write('\n')
          self.response.write(p1 + p2)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)