# '''
# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Blanka.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: L
# '''

# import urllib.request, urllib.parse, urllib.error

# from bs4 import BeautifulSoup

# url = input('Enter Url: ')
# if len(url) <= 0:
#     url = 'http://py4e-data.dr-chuck.net/known_by_Billy.html'

# position = int(input("Enter position: "))
# count = int(input("Enter count: "))

# counts = 0
# progress = '-'
# for i in range(count):
#     # print(i)
#     html = urllib.request.urlopen(url).read()
#     # print(f'html {html}')
#     # print()
#     soup = BeautifulSoup(html,'lxml')
#     # print(f'soup----------------------------------{soup}')

#     tags = soup('a')     # list of hrefs
#     # print(f'tags {tags}')
#     s = []
#     t = []
#     for tag in tags:
#         counts = counts + 1
#         x = tag.get('href', None)   # now extract the links <a hre />
#         # print(f'xval {x}')
#         s.append(x)  # place all the links into a list named s
#         y = tag.text
#         t.append(y) # place all the values in the link into link named t
#     url = s[position-1]
#     progress = progress + '-'
#     print(progress)

# print(s[position-1])
# print(t[position-1])

# # print(len(s))
# # # print()
# # print(len(t))

# print(f'{counts} iteration(s)')

