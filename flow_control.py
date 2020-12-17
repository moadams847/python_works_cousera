# # # us floor starts  from 1
# # # european floor numbering begins with 0

# # in_ = input('Enter European floor: ')
# # usf = int(in_) + 1
# # print('US floor is: ', usf)


# # conditonals

# # exxeption handling
# for i in range(5):
#     print(i)


# astr = 'hello Adams'
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('First', istr)


# astr =123
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print('second', astr)


# input_num = input('Enter a number: ')
# try:
#     intval = int(input_num)
# except:
#     intval = -1

# if intval > 0:
#     print('Nice work')
# else:
#     print('it is not a number')

# # while loop
# n = 2
# while n < 15:
#     print(n,'is even')
#     n = n + 2
# print('iteration is complete... ')

# hrs = input("Enter Hours: ")
# rph = input('Enter rate per hour: ')


# catch the error
# try:
#     h = float(hrs)
#     rate = float(rph)
# except:
#     print('Error, please enter numeric input')
#     quit()

# print(h,rate)
# if h==40:
#     regular = h * rate
#     print(regular)
# elif h > 40:
#     regular = h * rate
#     overtime = (h - 40) * (rate * 0.5)
#     pay = regular + overtime
#     print('pay is :' ,pay)

# print('Done')


# score = input("Enter Score: ")
# value = float(score)

# if value <= 0:
#     print('Error, score must be between 0 and 1')
#     quit()
# elif value >= 1:
#     print('Error, score must be between 0 and 1')
#     quit()

    
# if value >= 0.9:
#     print('A')
# elif value >= 0.8:
#     print('B')
# elif value >= 0.7:
#     print('C')
# elif value >= 0.6:
#     print('D')
# elif value < 0.6:
#     print('F')

# odd or even
# num_in = input('Enter any positive number: ')
# po_num = int(num_in)

# if po_num <= 0:
#     print('Error, please enter a number greater than zero.')
#     quit()

# if po_num % 2 == 0:
#     print(po_num,'is an even number.')
# elif po_num % 2 != 0:
#     print(po_num,'is an odd number.')
# print('You may enter another number.')
# print('Thank you.')

# ------------------------- updated--------------------------------------------

# score = input("Enter Score: ")
# value = float(score)

# try:
#     value <= 0
#     value >=1
# except:
#     print('Error, score must be between 0 and 1')   
#     quit()

# if value >= 0.9:
#     print('A')
# elif value >= 0.8:
#     print('B')
# elif value >= 0.7:
#     print('C')
# elif value >= 0.6:
#     print('D')
# elif value < 0.6:
#     print('F')

# even or odd
# num_in = input('Enter any positive number: ')
# po_num = int(num_in)

# if po_num <= 0:
#     print('Error, please enter a number greater than zero.')
#     quit()

# if po_num % 2 == 0:
#     print(po_num,'is an even number.')
# elif po_num % 2 != 0:
#     print(po_num,'is an odd number.')
# print('You may enter another number.')
# print('Thank you.')


# compute pay -----------------------------------------------

# def compute_pay(h,rate):
#     if h==40:
#         regular = h * rate
#         return regular

#     elif h > 40:
#         regular = h * rate
#         overtime = (h - 40) * (rate * 0.5)
#         pay = regular + overtime
#         return pay

# hrs = input("Enter Hours: ")
# rph = input('Enter rate per hour: ')

# h = float(hrs)
# rate = float(rph)

# p = compute_pay(h,rate)
# print('pay',p)

# loops or interations
# while anf for

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('blast off')
# print(n)

# using break and continue in a while loop--------------------------
# n = 5
# while n > 0:
#     line = input('input a text: ')
#     if line == 'done':
#         break
#     print(line)

# print('Done')


#  using break and continue key words
# n = 5
# while n > 0:
#     line = input('input a text: ')
#     if line[0]=='#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# # the above is the code block
# print('Done!')

# FOR LOOPS = DEFINITE ITERATIONS------------------------------
# for i in [5,4,3,2,1]:
#     print(i)

# ---------------------------------------------------------------
# friends = ['Adams','Aziz','Bintu']
# for friend in friends:
#     print('Happy New Year:', friend)
 
# print('Done!')
 

# for i in [1,3,5,7,9]:
#      print(i+1)


# n = 10
# while n > 0:
#     print(n)
#     n = n - 2


# finding the largest value---------------------------------
# largest_so_far = -1
# print('Before', largest_so_far)

# for the_num in [9,41,12,3,74,15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# print('After', largest_so_far)

# finding the smallest number
# smallest_so_far = 1
# print('Before', smallest_so_far)
# for the_num in [9,41,12,3,74,15,-2]:
#     if the_num < smallest_so_far:
#         smallest_so_far = the_num
#     print(the_num,smallest_so_far)
# print('After', smallest_so_far)


# counting in a loop
# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#     zork = zork + 1
#     print(zork,thing)
# print('After',zork)

# summing in a loop
# zork = 0
# print('Before', zork)
# for thing in [9,41,12,3,74,15]:
#     zork = zork + thing
#     print(zork, thing)
# print('After', zork)


# finding the average in a loop
# count = 0
# sam = 0

# print('Before', count, sam)
# for value in [9,41,12,3,74,15]:
#     count = count + 1
#     sam  = sam + value
#     print(count, sam, value)
# print('After',count, sam, sam / count)

# filtering in a loop

# print('Before')
# for value in [9,41,12,3,74,15]:
#     if value > 20:
#         print('Large number', value)
# print('After') 

# search using a boolean variable
# found = False
# print('Before', found)
# for value in [9,41,12,3,74,15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)


# search using a boolean variable with the break key word
# found = False
# print('Before', found)
# for value in [9,41,12,74,15,3]:
#     if value == 3:
#         found = True
#         break
#     # if 3 is found just jump out of the loop
#     # and print true
#     print(found, value)
# print('After', found)

# # finding the smallest number
 
# smallest_so_far = None 
# print('Before', smallest_so_far)

# for value in [9,41,12,3,74,15]:
#     if smallest_so_far is None:
#         smallest_so_far = value
#     elif value < smallest_so_far:
#         smallest_so_far = value
#     print(smallest_so_far, value)
      
# print('After', smallest_so_far)

# # finding the biggest number
# big = None
# print('Before',big)
# for value in [9,41,12,3,74,15]:
#     if big is None:
#         big = value
#     elif value > big:
#         big = value
#     print(big,value)
# print('After', big)


# worked exercise 5.1
# num = 0
# tot = 0.0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input')
#         continue
#     # print(fval)
#     num = num + 1
#     tot = tot + fval
  
# print('All Done')
# print(tot, num, tot / num)


# # worked exercise modified
# count = 0
# tot = 0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Error, invalid input!!!')
#         continue
#     # print(fval)
#     tot = tot + fval
#     count = count + 1
# print('-----------------------------')
# print('-----------------------------')
# print('-----------------------------')
# print('The sum is: ', tot)
# print('The average is: ', tot / count)
# print('Total iterations: ', count)
# print('All Done')

# exercise 5.2
# largest = None
# smallest = None

# while True:
#     # begining of code block
#     num = input("Enter a number: ")
#     if num == "done": 
#         # print(num)
#         break
#     try:
#         fnum = int(num)
#     except:
#         print('Invalid input')
#         continue

#     if largest is None:
#         largest = fnum
#     elif fnum > largest:
#         largest = fnum
#     elif smallest is None:
#         smallest = fnum
#     elif fnum < smallest:
#         smallest = fnum
#     print(largest,smallest,fnum)
    
    
#     # end of code block

# print('-------------------------')
# print('-------------------------')
# print('-------------------------')


# print('Invalid input')
# print("Maximum is", largest)
# print("Minimum is", smallest)

# hrs = input("Enter Hours: ")
# hr = float(hrs)

# rph = input('Enter rph: ')
# hp = float(rph)

# pay = hr*hp
# print('Pay:', pay)

