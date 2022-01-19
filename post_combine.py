from cgitb import text
import requests
from bs4 import BeautifulSoup
from time import sleep
import re
from xml.dom import minidom
import os
import random

def load_links(link_filename):
  with open('post_content' + os.sep + link_filename, 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    return lines


def data2xml(permaID, post_content, post_reaction, post_comment):
  xmlfile = minidom.Document()
  node = xmlfile.createElement('d')
  node.setAttribute('n'  , 'post_' + permaID)
  node.setAttribute('book'  , permaID)
  node_text = xmlfile.createTextNode(post_content)
  node.appendChild(node_text)
  xmlfile.appendChild(node)
  return xmlfile

if __name__ == '__main__':
  with open('allpost.xml', 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><b n="articles_modified" book="">  <b n="articles_modified">\n')
  for filename in os.listdir('post_content'):
    with open('allpost.xml', 'a') as f:
      f.write('<l>')
    contents = load_links(filename)
    for content in contents:
      content = str(content).encode('utf-8','ignore').decode("utf-8")
      with open('allpost.xml', 'a') as f:
        f.write(content + ' ')
    with open('allpost.xml', 'a') as f:
      f.write('</l>\n')
  with open('allpost.xml', 'a') as f:
      f.write('</b></b>')