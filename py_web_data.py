# regualar expressions
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)

# now using reg ex
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

# using search instead of start with
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From:', line):
#         print(line)

# extracting data using regular expressions
# import re

# # extract every number in the sentence
# x = 'My 2 favourite numbers are 78 and 93'
# y = re.findall('[0-9]+', x)
# print(y)

# # find every character upper case vowel in the sentence many times
# y = re.findall('[AEIOU]+', x)
# # since it doesnt contain any upper case vowel hence an empty list
# print(y)
# import re
# x = 'From adams@gmail.com sat Jan 5 09:34:33 2008'
# y = re.findall('\S+@\S+', x)
# print(y)

# adding parenthesis to the search
# the parenthesis tells us where to start and where to stop
# import re
# z = 'From adams@gmail.com sat Jan 5 09:34:33 2008'
# h = re.findall('^From (\S+@\S+)',z)
# print(h)

# t = re.findall('@([^ ]*)',z)
# print(t)

# more cooler version
# k = re.findall('^From .*@([^ ]*)', z)
# print(k)

# regex and loops
# import re
# hand = open('mbox-short.txt')
# num_list = list()
# for line in hand:
#     line = line.strip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     # print(stuff)
#     if len(stuff) < 1:
#         continue
#     # print(stuff)
#     num = float(stuff[0])
#     # print(num)
#     num_list.append(num)
# print('List', num_list)
# print('Maximum: ', max(num_list))


# # # regex and loops----------------------------------------------------
# # reg ex assignment trial
# count = 0
# num = 0
# x = 0
# empty_list = list()
# import re
# hand = open('sum_regex.txt')
# num_list = list()
# for line in hand:
#     num = num + 1
#     line = line.strip()
#     stuff = re.findall('([0-9]+)', line)
#     if len(stuff) <= 0:
#         continue
#     elif len(stuff) > 0:
#         count = count + 1
#         # print(stuff)
    
#     for i in stuff:
#         x = x + 1
#         empty_list.append(int(i))
# tot = sum(empty_list)
# print('There are', x , 'values with a sum=' + str(tot))


# print('-------------------------------------------')
# print('-------------------------------------------')


# print('complete_list',empty_list)       
# print(num, 'Iteration(s)')
# print(count,'List(s)')

# # # regex and loops---------------------------------------------------------
# # reg ex assignment proper
# count = 0
# num = 0
# x = 0
# tot = 0
# empty_list = list()
# import re
# hand = open('sum_regex_ass.txt')
# num_list = list()
# for line in hand:
#     num = num + 1
#     line = line.strip()
#     stuff = re.findall('([0-9]+)', line)
#     if len(stuff) <= 0:
#         continue
#     elif len(stuff) > 0:
#         count = count + 1
#         # print(stuff)
    
#     for i in stuff:
#         # print(i)
#         x = x + 1
#         tot = tot + int(i)
#         print(tot)
        
# print('There are', x , 'and the sum ends with',tot)


# print('-------------------------------------------')
# print('-------------------------------------------')


# print(num, 'Iteration(s)')
# print(count,'List(s)')


# networked technology--------------------------------------------------

# networking quiz
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(513)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()


# unicode characters and strings---------------------------------------
# print(ord('H'))

# want to make the socket code short------------------------------------
# since http is so common we have, we have a library that does
# all the socket work for us and makes web pages look like a file

# import urllib.request, urllib.parse, urllib.error

# fhand =urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

# make a dictionary using web data
# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# count = dict()
# for line in fhand:
#     words = line.decode().split()
#     # print(words)
#     for word in words:
#         count[word] = count.get(word, 0) + 1
# print(count)


# web scraping using beautiful soup and urllib----------------------------

# the code below tell the program to look into that path
# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter- ')

# if len(url) <= 0:
#     url = 'http://www.dr-chuck.com/page2.htm'

# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# # retrieve all of the ancho tags---------------------------------
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href',None))

# webscraping exercise using beautiful soup and urllib-----------------------

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # ignore ssl certificate------------------------------------------------
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter- ')

# if len(url) <= 0:
#     url = 'http://www.dr-chuck.com'

# # read the entire page
# html = urllib.request.urlopen(url, context = ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # retrieve all of the ancho tags
# count = 0
# tags = soup('a')
# for tag in tags:
#     count = count + 1
#     print(tag.get('href',None))
# print(count, 'Iteration(s)')


# # web scraping exercise using url lib and beautiful-------------------------------
# # scraping html data

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # ignore ssl certificate--------------------------------------------------
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter- ')

# if len(url) <= 0:
#     url = 'http://py4e-data.dr-chuck.net/comments_42.html'

# # read the entire page
# html = urllib.request.urlopen(url, context = ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup)

# # # retrieve all of the ancho tags-------------------------------------
# # count = 0
# tags = soup('span')

# count = 0
# comments = list()
# # print(tags)
# for tag in tags:
#     count = count + 1
#     tag.get('class',None)
#     tag.contents[0]
#     comments.append(int( tag.contents[0]))
# tot = sum(comments)
# print('sum='+ '' + str(tot))
# print(count, 'Iteration(s)')

# web scraping exercise using url lib and beautiful (real)-----1------------------
# scraping html data----2------------

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # ignore ssl certificate---------------------------------------------
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter- ')

# if len(url) <= 0:
#     url = 'http://py4e-data.dr-chuck.net/comments_1046551.html'

# # read the entire page
# html = urllib.request.urlopen(url, context = ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup)

# # # retrieve all of the ancho tags-----------------------------------------
# # count = 0
# tags = soup('span')

# count = 0 #counter
# tot = 0  # for summation
# # print(tags)
# for tag in tags:
#     count = count + 1
#     tag.get('class',None)
#     #tag.contents[0]
#     tot = tot + int(tag.contents[0])
    
# print('sum='+ '' + str(tot))
# print(count, 'Iteration(s)')


# web scraping exercise using url lib and beautiful (real)-----2--------------------
# scraping html data----2-------------------------------







# webscraping with corey schafer-------------------------------------------
# ---------------------------------------------------------------------------

# scraping from a webiste on your local machine-----------------------

# from bs4 import BeautifulSoup
# import requests

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# # print(soup.prettify())
# count = 0
# for article in soup.find_all('div', class_ = 'article'):
#     count = count + 1
#     #print(article)
#     headline = article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()
# print(count, 'iteration(s)')
 
# now pull data from an actual website-----------------------------------
# -----------------------------------------------------------------------

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('http://coreyms.com').text

# soup = BeautifulSoup(source, 'lxml')

# # counting
# counter = 0

# # writing to a csv file-------------
# csv_file = open('cms.scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])


# for articles in soup.find_all('article'): # find all articles
#     counter = counter + 1
    
#     headline = articles.h2.a.text   #extract the headline
#     print(headline)

#     summary = articles.find('div', class_ = 'entry-content').p.text
#     # find all div with class = entry-content, extract the 
#     # text from the p  tag
#     print(summary)
    
#     vid_src = articles.find('iframe', class_= 'youtube-player')
#     print(vid_src)
        
#     try:
#         vid_src = articles.find('iframe', class_= 'youtube-player')
#         vid_src_extract = vid_src['src']
#         vid_id = vid_src_extract.split('/')
#         broken_link = vid_id[4]
#         extract_id = broken_link.split('?')
#         id_ = extract_id[0]

#         yt_link = f'https://youtube.com/watch?v={id_}'
    
#     except:
#         yt_link = None
#     print(yt_link)

#     print('----------------------------', counter)

#     csv_writer.writerow([headline, summary, yt_link])

# print(f'{counter} iteration(s)')
# csv_file.close()

# ------------------------------------------------------------------------------

# my way without try and except---------------------------------------
# using if , else and continue ---------------------------------------

# now pull data from an actual website-----------------------------------

# imports and sys path
# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')
# from bs4 import BeautifulSoup
# import requests
# import csv

# # pull the html docs and pass it to beautiful soup
# source = requests.get('http://coreyms.com').text
# soup = BeautifulSoup(source, 'lxml')

# # start looping over the tags
# # counting
# counter = 0
# for articles in soup.find_all('article'):
#     counter = counter + 1
    
#     headline = articles.h2.a.text
#     print(headline)

#     summary = articles.find('div', class_ = 'entry-content').p.text
#     print(summary)
    
#     vid_src = articles.find('iframe', class_= 'youtube-player')
#     if vid_src == None:
#         continue
#     else:
#         vid_src_extract = vid_src['src']
#         vid_id = vid_src_extract.split('/')
#         broken_link = vid_id[4]
#         extract_id = broken_link.split('?')
#         id_ = extract_id[0]
#         yt_link = f'https://youtube.com/watch?v={id_}'
#         print(yt_link,'------------------',counter)

#     print('----------------------------',counter)
# print(f'{counter} iteration(s)')


# using the request library
# corey schafer--------------------------------
# request web pages, download images, Post data-----------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# from requests_html import HTML

# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html = source)
# # print(html.html)
# # print(html.text)

# # match = html.find('title')
# # print(match[0].text)

# articles = html.find('div.article')
# for article in articles:

#     headline = article.find('h2', first=True).text
#     summary = article.find('p',first=True).text
#     print(headline)
#     print(summary) 
#     print()

# grab data from an actual website----------------------------------
# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import csv
# from requests_html import HTML, HTMLSession

# # with open('simple.html') as html_file:
# #     source = html_file.read()
# #     html = HTML(html = source)

# csv_file = open('cms__scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video'])

# session = HTMLSession()
# r = session.get('https://coreyms.com/')

# articles = r.html.find('article')

# counter = 0
# for article in articles:
#     counter = counter + 1
    
#     headline = article.find('.entry-title-link', first=True).text
#     print(f'counts {counter}')
#     print(headline)

#     summary = article.find('.entry-content p', first=True).text
#     print(summary)

#     vid_src = article.find('iframe', first=True)
#     if vid_src == None:
#         print('-------------------------------------------------------------')
#         print('-------------------------------------------------------------')
#         continue
#     else:
#         vid_src_ = vid_src.attrs['src']
#         # print(vid_src_)
#         vid_id = vid_src_.split('/')[4]
#         vid_id = vid_src_.split('?')[0]
#         print(vid_id)

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#         print(yt_link)
#         print('-------------------------------------------------------------')
#         print('-------------------------------------------------------------')
        
#         csv_writer.writerow([headline, summary, yt_link])
# csv_file.close()

# print(f'{counter} Iteration(s)')


# xml---------------------------------------------------------------

# import xml.etree.ElementTree as ET

# input ='''

# <stuff>
#     <users>
#        <user x="2">
#         <id>001</id>
#         <name>Chuck</name>
#    </user>
#    <user x="7">
#        <id>009</id>
#        <name>Brent</name>
#        </user>
#    </users>

# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get("x"))

# xml exercise-----------------------------------------------------

# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import urllib
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET

# url = input("Enter: ")

# if len(url) < 1:
#     url = 'http://py4e-data.dr-chuck.net/comments_1046553.xml'

# data = urllib.request.urlopen(url).read()

# tree = ET.fromstring(data)
# results = tree.findall('comments/comment')
# count = 0
# tot = 0
# for item in results:
#     x = int(item.find('count').text)
#     count = count + 1
#     tot = tot + x

# print(f'Sum={tot}')
# print(f'Average={tot/count}')
# print(f'{count} Iteration(s)')


# etract data from json----------------------------------------------
# with dictionary
# import sys
# sys.path.append('/users/adams/anaconda3/lib/site-packages')

# import json

# data = '''{
# "name" : "Chuck",
# "phone" : {
# "type" : "intl",
# "number" : "+1 734 303 4456"
# },
# "email" : {
# "hide" : "yes"
# }
# } '''

# info = json.loads(data)
# print('Name:', info['name'])
# print('Hide:', info['email']['hide'])

# with a list
# it means we can iterate through

import sys
sys.path.append('/users/adams/anaconda3/lib/site-packages')

import json

# input = '''[

# { "id" : "001",
# "x" : "2",
# "name" : "Chuck"
# } ,

# { "id" : "009",
# "x" : "7",
# "name" : "Chuck"
# }

# ]'''

# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('ID', item['id'])
#     print('Attribute', item['x'])
#     print()
# print('Done')
# print()


# service oriented approach
# using application programing interfaces-------------------------------

import urllib.request, urllib.parse, urllib.error
import  json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    
    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print(f'Retrived {len(data)} characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('========= Failure To Retrive')
        print(data)
        continue
    
    print(json.dumps(js, indent=4))
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)









