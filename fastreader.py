#!/usr/bin/env python

import sys, getopt
import nltk
import os
import time

def parse_words_from_file(path):
  f = open(path, 'r')
  words = nltk.word_tokenize(f.read())

  return words

def main(argv):
  inputfile = ''

  try:
    opts, args = getopt.getopt(argv,"hi:o:",["input="])
  except getopt.GetoptError:
    print 'fastreader.py -i <inputfile>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print 'fastreader.py -i <textfile>'
      sys.exit()
    elif opt in ("-i", "--input"):
      inputfile = arg

  words = parse_words_from_file(inputfile)
  
  os.system('clear')
  for word in words:
    time.sleep(0.2) # For 300 words per minute
    print word

if __name__ == "__main__":
   main(sys.argv[1:])