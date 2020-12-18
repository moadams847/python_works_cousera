# unicode charaters and strings-------18/12/20-----------------------
# x = 'abc'
# # print(type(x))
# print(dir(x))

# # our first class and object-----------------------------
 
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
# j = partyAnimal('Sally')
# j.party()
# s.party()

#  inheritance-------------------------------------------

class partyAnimal:
    x = 0
    name = ""
    def __init__(self,nam):
        self.name = nam
        print(f'{self.name} constructed')

    def party(self):
        self.x = self.x + 1
        print(f'{self.name} party count {self.x}')

class FootballFan(partyAnimal):
    point = 0
    def touchdown(self):
        self.point = self.point + 7
        self.party()
        print(f'{self.name} points {self.point}')

s = partyAnimal('sally')
s.party( ) 
print()

j = FootballFan('Jim')
j.party()
j.touchdown()














