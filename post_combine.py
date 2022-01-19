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
  for filename in os.listdir('post_content'):
      contents = load_links(filename)
      print(contents[0])
      with open('allpost.txt', 'a') as f:
        for content in contents:
          f.write(content + ' ')
        f.write('\n')