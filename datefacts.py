import nltk.data
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import sys
import re
import os

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
extra_abbreviations = ['m.a', 'm. a', 'ph.d', 'ph. d', 'rev', 'm.i.t' , 'litt.d', 'm.d', 'a.b', 'ph.b', 'b.a', 'll.b', 'll.d', 'sc.b', 'y.m.c.a', 'l.h.d', 'u.c.a', 'g.o.p', 'n.e.i.s.a', 'd.d', 'm.s']
tokenizer._params.abbrev_types.update(extra_abbreviations)


for line in sys.argv:
  def filename_to_title(path):
    return re.sub(r'.html', '', os.path.basename(path))
      
      
  def title_to_name(title):
    split = title.split(",")
    return split[1].strip() + ' ' + split[0].strip()

  r = re.compile('[1-9][0-9][0-9][0-9]')
  fp = open(line, 'r').read()
  data = re.sub('<i>', '“', fp)
  data = re.sub('</i>', '”', data)
  data = re.sub('<p>', ' ', data)
  data = re.sub('</p>', ' ', data)
  data = re.sub('<b>', '', data)
  data = re.sub('</b>', '', data)
  #data = re.sub(':', '.', data)
  data = re.sub('“', '"', data)
  data = re.sub('”', '"', data)
  data = re.sub('<blockquote>.+</blockquote>', '', data)
  data = re.sub('<h2>.+</h2>', '', data)
  #data = re.sub('<[^<]+?>', ' ', data)
  
# abrevs: Rev.
  def fixpro(txt):
    title = filename_to_title(line)
    cite = '<cite>' + '<a href="'+ os.path.basename(line) + '">' + title + '</a></cite>'
    if not(re.match(r'.+,.+', title)):
      return txt.strip() + cite
    else:
      name = title_to_name(title)
      
      def contains_name(n, t):
        name_bits = n.split(' ')
        first = name_bits[0]
        last  = name_bits[len(name_bits) - 1]
        if t.find(first.strip()) != -1 or t.find(last.strip()) != -1:
          return True
        else:
          return False
          
      # can we remove 'also' before a period?
      # edge case: 'for her.'; it's not possessive. ugh english.
      if not(contains_name(name, txt)):
        txt = re.sub(r'\b(((S|s)h)|(H|h))e\b', name, txt, 1)
      if not(contains_name(name, txt)):
        txt = re.sub(r'\b(H|h)((is)|(er))\b', name + "'s", txt, 1)
      return txt.strip() + cite
      
  print('\n'.join(map(fixpro,filter(r.search, tokenizer.tokenize(data, realign_boundaries=True)))))
