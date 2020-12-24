# unicode charaters and strings-------18/12/20-----------------------
# x = 'abc'
# # print(type(x))
# print(dir(x))

# our first class and object-----------------------------
 
# class partyAnimal:
#     x = 0

#     def party(self):
#         self.x = self.x + 1
#         print('so far',self.x)

# an = partyAnimal()  
# an.party()
# an.party()  
# an.party()
# an.party()   
 
# object life cycle-----------------------
# class partyAnimal:
#     x = 0

#     def __init__(self): 
#         print('I am constructed')

#     def party(self):
#         self.x = self.x + 1
#         print('so far',self.x)

#     def __del__(self):
#         print('I am destructed at', self.x)

# an = partyAnimal()
# an.party() 
# an.party()
# an = 42
# print('an contains', an)
 
# many instances---------------------------
# class partyAnimal:
#     x = 0
#     name = ""

#     def __init__(self,z):
#         self.name = z
#         print(f'{self.name} constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(f'{self.name} party count {self.x}')

# s = partyAnimal('Jim')
# s.party( ) 
# print()
# j = partyAnimal('Sally' )
# j.party()
# s.party()

#  inheritance-------------------------------------------
# class partyAnimal:
#     x = 0
#     name = ""
#     def __init__(self,nam):
#         self.name = nam
#         print(f'{self.name} constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(f'{self.name} party count {self.x}')

# class FootballFan(partyAnimal):
#     point = 0
#     def touchdown(self):
#         self.point = self.point + 7
#         self.party()  # method from party animal class
#         print(f'{self.name} points {self.point}')

# s = partyAnimal('sally')
# s.party( ) 
# s.party()
# print()
# j = partyAnimal('Jim')
# j.party()
# j.party()

# j = FootballFan('Jim')
# j.party()
# j.touchdown()

# teluako--------------youtuber-------------
# class Computer:
# #  attributes/data/variables
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
 
# # methods/functions 
#     def config(self):
#         print('config is', self.cpu, self.ram)

# # objects of computer class  
# com1 = Computer('i5', 16) 
# com2 = Computer('ryzen 3',8) 

# # instances or objects
# com1.config()
# com2.config()

# types of variables-----------------------------
# -----------------------------------------------

# car class 
# class Car:

# # class variable
#     wheels = 4

# #  instance variables
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BMW'

# # car objects
# c1 = Car()
# c2 = Car()

# # class varible change
# Car.wheels = 5

# # handling objects
# print(c1.mil, c1.com, c1.wheels)
# print(c2.mil, c2.com, c2.wheels)

# types of methods in pythoon------------------------------------
# ---------------------------------------------------------------

# students class
# class Students:

# # static variable or instance variable----------------------------
#     school = 'Adams Analytics'

# # instance variables/attributes ------------------------------------
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
# # instance method (mutator) == setters-----------------------------------
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

# # instance method (getter) == fetch ----------------------------------
#     def get_m1(self):
#         return self.m1

# # instance method (setters) ----------------------------------------
#     def set_m1(self,value):
#         self.m1 = value
#         return value

# # class methods-----------------------------------------------------   
#     @classmethod
#     def getSchoolname(cls):
#         return cls.school

# # static methods ----------------------------------------------------
#     @staticmethod
#     def info():
#         print('This is Students class in Abc Module')

# # objects 
# s1 = Students(34,67,32)
# s2 = Students(89,32,67)

# # print(s1.m1)
# # print(s2.m1)

# print(s1.avg())
# print(s2.avg())
# print(s1.get_m1())
# print(s1.set_m1(100))
# print(Students.getSchoolname())
# Students.info()


# inheritance-------------------------------------------------
# here, B is a child class of A
# ie B inherits A

# class A:
#     def feature1(self):
#         print('Feature 1')
    
#     def feature2(self):
#         print('Feature 2')

# class B(A):
#     def feature3(self):
#         print('Feature 3')
    
#     def feature4(self):
#         print('Feature 4')

# # multiilevel inheritance--
# class C(B):
#     def feature5(self):
#         print('Feature 5')

# # objects or instances
# a1 = A()
# a1.feature2()
# a1.feature2()

# b1 = B()
# b1.feature4()
# b1.feature4()

# c1 = C()
# c1.feature5()

# constructor in inheritance----------------------
#  methos resolution order
# class A:
#     def __init__(self): 
#         print('in A init')
        
#     def feature1(self):
#         print('Feature 1')
    
#     def feature2(self):
#         print('Feature 2')

# class B(A):

# # init of B
#     def __init__(self): 

#         # calling the init from A
#         super().__init__()
#         print('in B init')
 
#     def feature3(self):
#         print('Feature 3')
    
#     def feature4(self):
#         print('Feature 4')

# # a1 = A()
# b1 = B()


# relational databases---------------------------------------------
# using databases -------------------------------------------------
# single tabke crud---------------------

# counting org in a database-------------------
# unicode charaters and strings-------18/12/20-----------------------
# x = 'abc'
# # print(type(x))
# print(dir(x))

# our first class and object-----------------------------
 
# class partyAnimal:
#     x = 0

#     def party(self):
#         self.x = self.x + 1
#         print('so far',self.x)

# an = partyAnimal()  
# an.party()
# an.party()  
# an.party()
# an.party()   
 
# object life cycle-----------------------
# class partyAnimal:
#     x = 0

#     def __init__(self): 
#         print('I am constructed')

#     def party(self):
#         self.x = self.x + 1
#         print('so far',self.x)

#     def __del__(self):
#         print('I am destructed at', self.x)

# an = partyAnimal()
# an.party() 
# an.party()
# an = 42
# print('an contains', an)
 
# many instances---------------------------
# class partyAnimal:
#     x = 0
#     name = ""

#     def __init__(self,z):
#         self.name = z
#         print(f'{self.name} constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(f'{self.name} party count {self.x}')

# s = partyAnimal('Jim')
# s.party( ) 
# print()
# j = partyAnimal('Sally' )
# j.party()
# s.party()

#  inheritance-------------------------------------------
# class partyAnimal:
#     x = 0
#     name = ""
#     def __init__(self,nam):
#         self.name = nam
#         print(f'{self.name} constructed')

#     def party(self):
#         self.x = self.x + 1
#         print(f'{self.name} party count {self.x}')

# class FootballFan(partyAnimal):
#     point = 0
#     def touchdown(self):
#         self.point = self.point + 7
#         self.party()  # method from party animal class
#         print(f'{self.name} points {self.point}')

# s = partyAnimal('sally')
# s.party( ) 
# s.party()
# print()
# j = partyAnimal('Jim')
# j.party()
# j.party()

# j = FootballFan('Jim')
# j.party()
# j.touchdown()

# teluako--------------youtuber-------------
# class Computer:
# #  attributes/data/variables
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
 
# # methods/functions 
#     def config(self):
#         print('config is', self.cpu, self.ram)

# # objects of computer class  
# com1 = Computer('i5', 16) 
# com2 = Computer('ryzen 3',8) 

# # instances or objects
# com1.config()
# com2.config()

# types of variables-----------------------------
# -----------------------------------------------

# car class 
# class Car:

# # class variable
#     wheels = 4

# #  instance variables
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BMW'

# # car objects
# c1 = Car()
# c2 = Car()

# # class varible change
# Car.wheels = 5

# # handling objects
# print(c1.mil, c1.com, c1.wheels)
# print(c2.mil, c2.com, c2.wheels)

# types of methods in pythoon------------------------------------
# ---------------------------------------------------------------

# students class
# class Students:

# # static variable or instance variable----------------------------
#     school = 'Adams Analytics'

# # instance variables/attributes ------------------------------------
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
# # instance method (mutator) == setters-----------------------------------
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3

# # instance method (getter) == fetch ----------------------------------
#     def get_m1(self):
#         return self.m1

# # instance method (setters) ----------------------------------------
#     def set_m1(self,value):
#         self.m1 = value
#         return value

# # class methods-----------------------------------------------------   
#     @classmethod
#     def getSchoolname(cls):
#         return cls.school

# # static methods ----------------------------------------------------
#     @staticmethod
#     def info():
#         print('This is Students class in Abc Module')

# # objects 
# s1 = Students(34,67,32)
# s2 = Students(89,32,67)

# # print(s1.m1)
# # print(s2.m1)

# print(s1.avg())
# print(s2.avg())
# print(s1.get_m1())
# print(s1.set_m1(100))
# print(Students.getSchoolname())
# Students.info()


# inheritance-------------------------------------------------
# here, B is a child class of A
# ie B inherits A

# class A:
#     def feature1(self):
#         print('Feature 1')
    
#     def feature2(self):
#         print('Feature 2')

# class B(A):
#     def feature3(self):
#         print('Feature 3')
    
#     def feature4(self):
#         print('Feature 4')

# # multiilevel inheritance--
# class C(B):
#     def feature5(self):
#         print('Feature 5')

# # objects or instances
# a1 = A()
# a1.feature2()
# a1.feature2()

# b1 = B()
# b1.feature4()
# b1.feature4()

# c1 = C()
# c1.feature5()

# constructor in inheritance----------------------
#  methos resolution order
# class A:
#     def __init__(self): 
#         print('in A init')
        
#     def feature1(self):
#         print('Feature 1')
    
#     def feature2(self):
#         print('Feature 2')

# class B(A):

# # init of B
#     def __init__(self): 

#         # calling the init from A
#         super().__init__()
#         print('in B init')
 
#     def feature3(self):
#         print('Feature 3')
    
#     def feature4(self):
#         print('Feature 4')

# # a1 = A()
# b1 = B()


# relational databases---------------------------------------------
# using databases -------------------------------------------------
# single tabke crud---------------------

# counting org in a database-------------------
# import sqlite3

# conn = sqlite3.connect('orgdb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'mbox.txt'
# fh = open(fname)
# count = 0
# for line in fh:
#     count = count + 1
#     if not line.startswith('From: '):
#         continue
#     line = line.strip()
#     pieces = line.split()
#     org = pieces[1]
#     # print(org)
#     cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#             VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#         (org,))
# conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])   
# cur.close()
# print(f'{count} interation(s)')


# exercise-----------------------------------------------------------
# import sqlite3

# conn = sqlite3.connect('orgdb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'mboxx.txt'
# fh = open(fname)
# count = 0
# for line in fh:
#     count = count + 1
#     if not line.startswith('From:'):
#         continue
#     line = line.strip()
#     pieces = line.split()
#     email = pieces[1]
#     pieces = email.split('@')
#     org = pieces[1]
#     # print(org)
#     cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#             VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#         (org,))

# #  commit outside the loop to make interation faster
# conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# sum_list = list()
# for row in cur.execute(sqlstr):
#     sum_list.append(int(row[1]))
#     print(str(row[0]), row[1]) 
# cur.close()
# print()
# print(sum_list)  
# sum__ = sum(sum_list)
# print(f'sum of top 10 organisational emails is {sum__}')
# print(f'{count} interation(s)')

# classes by corey schafer------------------------------
# POOP-----------------------------------------------
# class 
class Employee:
    
    # want to keep track of number of employees
    num_of_emps = 0

    # class variable
    raise_amount = 1.04

    # instance variables
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = f'{first_name}.{last_name}@company.com'

        Employee.num_of_emps = Employee.num_of_emps + 1
  
    # instance methods (getters)
    def fullName(self):
        return '{} {}'.format(self.first_name,self.last_name)
        # return f'{self.first_name, self.last_name}'  

    # instance methods (setters)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Adams', 'Mohammed', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



