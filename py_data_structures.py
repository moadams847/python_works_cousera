# strings------------------------
# fruit = 'banana'
# letter = fruit[0]
# print(letter)

# print(len(fruit))

# while loop----------------------
# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1
# print('Toal iterations:', index)   
# print('All Done')

# alternatiavely we can use a for loop------------------------
# count = 0
# fruit = 'banana'
# for letter in fruit:
#     print(count,letter)
#     count = count + 1
# print('total iteration', count)


# looping and counting
# word = 'banana'
# count = 0
# num = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
#     num = num +1
# print(count)
# print(num, 'iterations')

# slicing
# s = 'Monty Python'
# print(s[0:4])


# string manipulation
# a = 'Hello'
# b = a + 'There'
# print(b)

#  correct version
# a = 'Hello'
# b = a + ' ' + 'There'
# print(b)
 
# # in operator
# fruit = 'Banana'
# 'n' in fruit

# if 'a' in fruit:
#     print('Found it!')

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)

# # character type
# print(type(zap)) 

# print(greet)
# stuff = 'Hello world'
# print(type(stuff))

# methods we can perform on strings
# print(dir(stuff))


# the string library
# stuff = 'Hello world'
# a = str.capitalize(stuff)
# print(a)

# fruit = 'Banana'
# pos  = fruit.find('na')
# print(pos)
 
# greetings = 'Hello Bob'
# nstr = greet.replace('Bob','Jane')
# print(nstr)
# print(greetings)

# # white spaces
# greet = '    Hello Adams    '
# stripped = greet.lstrip()
# print(stripped)

# stripped = greet.rstrip()
# print(stripped)

# stripped = greet.strip()
# print(stripped)

# # parsing and extracting 
# data = 'From Adams.mohoammed@ug.edu.gh Sat Jan 09:14:16 2008'
# # finds the position of @
# atpos = data.find('@')
# print(atpos)

# # count the data but start from atpos
# sppos = data.find(' ',atpos)
# print(sppos)

# # now do the extraction
# host = data[atpos+1 : sppos]
# print(host)


# exercise 6.5
# text = "X-DSPAM-Confidence:    0.8475"
# # count upto the white space
# atpos = text.find(' ')
# print(atpos)

# sppos = text.find('5',atpos)
# print(sppos)

# strin_extract = text[atpos : sppos+1]
# # print(strin_extract)

# stripped = strin_extract.strip()
# # print(stripped)

# conv_float = float(stripped)
# print(conv_float)

# print(type(conv_float))


# reading files

# print('hello\nworld')

# count = 0
# fhand = open('words.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('from'):
#         print(line)
#     count = count + 1
# print(count, 'iterations')


# # alternative
# count = 0
# fhand = open('words.txt')
# for line in fhand:
#     line = line.rstrip()
#     count = count + 1
#     if not line.startswith('from'):
#         continue
#     print(line)
# print(count, 'iterations')
    

# # selecting lines
# count = 0
# fhand = open('words.txt')
# for lin in fhand:
#     lin = lin.rstrip()
#     count = count + 1
#     if not '@ug.edu.gh' in lin:
#         continue
#     print(lin)
# print(count, 'iterations')


# # prompts for file name
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit()

# count = 0
# num = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
#     num = num + 1
# print('There were', count, 'subjects in', fname)
# print(num, 'iterations')

# exercise 7.1
# Use words.txt as the file name
# count = 0
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     line = line.upper()
#     line = line.rstrip()
#     print(line)
#     count = count + 1
# print(count,'iterations')

# exercise 7.2
# Use the file name mbox-short.txt as the file name
# n = 0 # to count all iterations
# m = 0 # to  count the iterations of interest
# total = 0 # iterations for summmation

# fname = input("Enter file name: ")
# fh = open(fname)

# for line in fh:
#     # begining of code block
#     m = m + 1 # counts the entire iteration
#     if not line.startswith("X-DSPAM-Confidence:") : 
#         continue
#     atpos = line.find(':')
#     extract = line[atpos+1:]
#     rm_white_space = extract.strip()
#     conv_float = float(rm_white_space)
#     total = conv_float + total
#     #print(summation)
#     n = n + 1 #counts the line of interest
#     # end of code block

# print('--------------------------------')
# print('--------------------------------')

# print('The total spam confidence:', total)
# print('The Average spam confidence:', total / n)

# print('--------------------------------')
# print('--------------------------------')

# print(n,': Iterations are needed to find the line of interest')
# print(m,': Total iterations')
# print("Done")


# list----------------------------------------------------
# print(range(4))
# friends = ['Adams', 'Glenn', 'Sally']

# for i in range(len(friends)):
#     friend = friends[i]
#     print('Happy New Year:', friend)

# # manipulating strings
# t = [9,41,12,3,74,15]

# slicing of list
# print(t[1:3]) # position 2 to 3

# print(t[:4]) # position 1 to 3

# print(t[3:]) # from the 4th position to the end

# print(t[:]) # select everything from the list

# # just like string methods there 
# # there are list methods

# # list methods--------------------------------------
# stuff  = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# stuff.append('cookie')
# print(stuff)

# some = [0,7,6,6,3,4,5]
# print(7 in some)

# friends.sort()
# print(friends)

# loops with list
# this asks for user input and appends it to a 
# list and then prints out the the average and 
# total  = 0
# count = 0
# it = 0
# num = list()
# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     try:
#         value = float(inp)
#     except:
#         print('Error, Enter a number please!!!')
#         continue
#     numlist.append(value)
#     it = it + 1
#     num.append(it)
#     # it = it + 1
#     total = total + value
#     count = count + 1

# average = total / count
# print('list:' , numlist)
# print('count: ',num)
# print('Average: ', average)
# print('Length of the list_: ',count) 

# list and strings
# abc = 'with three words'
# stuff = abc.split()
# print(stuff)

 
# when you donot specify a delimiter, multiole spaces are treated like 
# one delimiter

# we can specify what delimeter charcter to use in the splitting

# line = 'A lot         of spaces'
# etc = line.split()
# print(etc)

# # not the right format
# line = 'First.second.third'
# thing = line.split()
# print(thing)

# # the right format
# thing = line.split('.')
# print(thing)

# the double spliting

# exercise 8.4
# numlist = list()
# count = 0
# while True:
#     inp = input('Please enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     count = count + 1
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print('Average: ', average)
# print(count, ': Iterations')

# stripping
# total = 0
# num = 0
# fhand = open('mbox-short.txt')
# for line in fhand:
#     total = total + 1
#     line = line.rstrip()
#     if not line.startswith('From'):
#         continue
#     num = num + 1
#     words = line.split()
#     print(words[1])
# print('-----------------------')
# print('-----------------------')
# print(total,': Total iterations')
# print(num, ': Iterations of interest')

# double split
# stripping
# total = 0
# num = 0
# fhand = open('mbox-short.txt')
# for line in fhand:
#     total = total + 1
#     line  = line.strip()
#     words = line.split()
#     email = words[1]
#     pieces = email.split('@')
#     print(pieces[0])


# print('-----------------------')
# print('-----------------------')
# print(total,': Total iterations')
#print(num, ': Iterations of interest')



# exercise 8.4 wrong----------------------------
# mistake
# fname = input("Enter file name: ")
# i = 0
# fh = open(fname)
# lis = list()
# for line in fh:
#     i = i + 1
#     line = line.rstrip()
#     appended = lis.append(line)
#     #line_of_words = line.split()


# exercise 8.4 corrected-----------------------------
# fname = input("Enter file name: ")
# fhand = open(fname)

# lines = fhand.readlines()
# myline = " ".join([line.strip() for line in lines])

# list = list()
# words = myline.split()
# for word in words:
#     if word not in list:
#         list.append(word)
#         list.sort()
# print(list)



# exercise 8.5
# fname = input("Enter file name: ")

# if len(fname) < 1 :
#      fname = "mbox-short.txt"

# fh = open(fname)

# num = 0
# count = 0
# for line in fh:
#     line = line.rstrip()
#     count = count + 1
#     if not line.startswith('From:'):
#         continue
#     words = line.split()
#     print(words[1])
#     num = num + 1
# print("There were",num , "lines in the file with From as the first word")
# print(count, 'Iterations')

# # exercise 8.5 solution from francis 
# fname = input("Enter file name: ")
# fhand = open(fname)
# count = 0
# for line in fhand:

#     if line.startswith("From:"):
#         continue
#     elif line.startswith("From"):
#         count = count + 1
#         line = line.rstrip()
#         xline = line.split()
#         email = xline[1]
#         print(email)
# print(count)

# debugging-----------------------------------------------------------------
# using another approach to select 'from' from the mbox-short.txt

# han = open('mbox-short.txt')
# count = 0
# for line in han:
#     count = count + 1
#     line =line.rstrip()
#     #print('Line:', line)

#     # another guardian
#     if line == '':
#         #print('skip blank')
#         continue

#     wds = line.split()
#     #print('words',wds)

#     # Guardian a bit stronger
#     # if len(wds) < 3: 
#     #     continue

#     #print(count, 'Iterations before it blew up')
#     if wds[0] != 'From' :
#         #print('ignore')
#         continue
#     print(wds[2])


# debugging-------------------------------------------------------------------
# using another approach to select 'from' from the mbox-short.txt
# compound statement

# han = open('mbox-short.txt')
# count = 0
# for line in han:
#     count = count + 1
#     line =line.rstrip()
#     wds = line.split() 
#     # guardian in a compound statement
#     if len(wds) < 3 or wds[0] != 'From' :
#         #print('ignore')
#         continue
#     print(wds[2])

# DICTIONARIES------------------------------------------------
# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# print(purse['candy'])

# purse['candy'] = purse['candy'] + 2
# print(purse['candy'])
# print(purse)

# empty dict
# ddd = dict()
# ddd['age'] = 21
# ddd['course'] = 189
# print(ddd)
# ddd['age'] = 34
# print(ddd)

# counting with dictionaries
# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)

# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc['cwen'])
# print(ccc)

# dictionary with conditional execution

# counts = dict()
# names = ['csev', 'cwen', 'zquian', 'cwen', 'csev']

# num = 0
# for name in names:
#     num = num + 1   #counter
#     if name not in counts:
#         counts[name] = 1
#     elif name in counts:
#         counts[name] = counts[name] + 1
        
# print(counts)
# print(num, 'Iterations')

# using the get method for dictionaries to make the code simple

# counts = dict()
# names = ['csev', 'cwen', 'zquian', 'cwen', 'csev']

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# dictionaries and files
# counts  = dict()
# print('Enter a line of text: ')
# line = input('')
# fhand = open(line)
# #print(fhand)

# num = 0
# for i in fhand:
#     num = num + 1
#     word=i.split(' ')
#     #print(word)
# print(num,'Iteration(s)')

# print('Initial Loop----------------')
# print('Words:',word)
# print('Counting...................')

# print('Second Loop-------------------')
# y = 0 # total iterations
# c = 0 #for unique
# for x in word:
#     y = y + 1
#     if x not in counts:
#         c = c + 1
#         counts[x] = 1
#     elif x in counts:
#         counts[x] = counts[x] + 1

# print('Counts', counts)
# print(c,'Unique Value(s)')
# print(y, 'Iteration(s)')

# looping over a dictionary in python

# count = 0
# counts = {'Adams':34, 'Francis':56, 'Obed':45}
# for key in counts:
#     count = count + 1
#     print(key, counts[key])
# print(count,'Iteration(s)')

# getting list of keys from a dictionary
# print(list(counts))

# # using the dictioanary method to get the list of keys and values
# print(counts.keys())
# print(counts.values())

# # using the item method to pull the key value pairs
# print(counts.items())

# # two iteration variables with the help of item method in dictionaries
# for i,j in counts.items():
#     print(i,j)

# put it together
# name  = input('Enter a file name: ')
# fhand = open(name)
# x = 0 #counts sentence
# y = 0 #counts words
# z = 0 #counts unique words
# counts = dict()
# for line in fhand:
#     x = x + 1 #counter
#     stripped_words = line.strip()
#     #print(stripped_words)
#     words = stripped_words.split(' ')
#     print(words)
#     for word in words:
#         y = y + 1 #counter
#         if word not in counts:
#             z = z + 1  #counter
#             counts[word] = 1
#         elif word in counts:
#             counts[word] = counts[word] + 1

# print('-----------------------------------')
# print('-----------------------------------')

# print('Counts: ', counts)
# print(x, 'Sentence(s)')
# print(z, 'Unique value(s)')
# print(y,'Word(s)')

# bigcount = None
# bigword = None
# for word, count in counts.items():
#     print(word,count) #want to see what happening 
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword,bigcount)

# # exercise 9.4 my solution
# counts = dict() #empty dictionary
# name = input("Enter file:")
# if len(name) < 1 : 
#     name = "mbox-short.txt"
# handle = open(name)
# for line in handle:
#     if line.startswith('From:'):
#         continue
#     elif line.startswith('From'):
#         stripped_line = line.rstrip()
#         split_line_word = stripped_line.split()
#         names = split_line_word[1]
#         counts[names] = counts.get(names,0) + 1
# #print('Counts:' ,counts)

# bigword = None
# bigcount  = None

# for email,frequency in counts.items():
#     if bigword is None or frequency > bigcount:
#         bigword = email
#         bigcount = frequency
# print(bigword,bigcount)

#exercise 9.4 solution from francis
# email_address = dict()
# fhand = open("mbox-short.txt")
# for line in fhand:
#     if line.startswith("From:"):
#         continue
#     elif line.startswith("From"):
#         line = line.rstrip()
#         pieces = line.split()
#         email = pieces[1]
#         email_address[email] = email_address.get(email,0) + 1
# print(email_address)

# most_count = None
# most_frequent_email = None
# for email, frequency in email_address.items():
#     if most_count is None or frequency > most_count:
#         most_frequent_email = email
#         most_count = frequency

# print(most_frequent_email, most_count)

# tuples
# (x,y) = (4,'fred')
# print(x)

# # sorting by key
# d = {'a':1,'b':222,'c':34}
# print(sorted(d.items()))

# for k,v in sorted(d.items()):
#     print(k,v)

# # # sorting by key order
# temp = list()
# for v,k in d.items():
#     temp.append((k,v))
# print(temp)

# temp = sorted(temp, reverse=True)
# print(temp)

# exercise 10.2
# tim_dict = dict()
# count = 0
# name = input("Enter file:")
# if len(name) < 1 :
#      name = "mbox-short.txt"
# handle = open(name)
# for line in handle:
#     line = line.rstrip()
#     # print(line)
#     if line.startswith('From:'):
#         continue
#     elif line.startswith('From'):
#         count = count + 1
#         pieces = line.find(':')
#         position = pieces - 2
#         # print(position)
#         position_another = line.find(' ', position)
#         #print(position_another)
#         time = line[position : position_another]
#         units_time = time.split(':')
#         extract = units_time[0]
#         tim_dict[extract] = tim_dict.get(extract,0) + 1

# for k,v in sorted(tim_dict.items()):
#     print(k,v)

# exercise 10.2 with reg ex
# import re
# tim_dict = dict()
# count = 0
# name = input("Enter file:")
# if len(name) < 1 :
#      name = "mbox-short.txt"
# handle = open(name)
# for line in handle:
#     line = line.rstrip()
#     # print(line)
#     stuff = re.findall('^From .+ ([0-9]+?:)', line)
#     print(stuff)
#     if len(stuff) <= 0:
#         continue
#     elif len(stuff) > 0:
#         sliced = stuff[0]
#         pieces = sliced.split(':')
#         hours = pieces[0]
#         print(hours)

    
# # worked exercise 10
fname = input('Enter File name: ')
if len(fname) < 1:
    fname = 'file.txt'
fhand = open(fname)

count_dict = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # print(words)
    for word in words:
        # print(word)
        if word not in count_dict:
            count_dict[word] = 1
        elif word in count_dict:
            count_dict[word] = count_dict[word] + 1
#print(count_dict)

# x = sorted(count_dict.items())
# print(x)


# here we want to change the order of the 
# dictionary from k,v to v,k
# temp = list()
# for k,v in count_dict.items():
#     # print(k,v)
#     newt = (v,k)
#     temp.append(newt)
# # print('Flipped',temp)

# temp = sorted(temp, reverse=True)
# # print('Sorted_reversed', temp[:5])

# for v,k in temp[:5]:
#     print(v,k)