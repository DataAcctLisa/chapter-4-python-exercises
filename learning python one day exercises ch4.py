# chapter 4

# question 1

name1 = 'Jamie'
print(name1)

name2 = 'Aaron'.upper()
print(name2)

message = 'The names are %s and %s.' %(name1, name2)
print(message)

# output should be
# Jamie
# Aaron
# The names are Jamie and AARON

lang1 = 'Python'
lang2 = 'Java'
lang3 = 'C#'

message1 = 'The most popular programming languages are %s, %s, and %s. '%(lang1, lang2, lang3)

message2 = 'The most popular programming languages are %s, %s, and %s. '%(lang1, lang3, lang2)

print(message1)
print(message2)

# Question 3

num = 12

message = '%d' %(num)
print(message)

message = '%4d' %(num)
print(message)

# output

# 12
#   12

#  %s is for string, %d is for integer %4 refers to total length
#  (which is why there's 2 spaces before 12 for total 4 spaces)

# question 4

decnum = 1.72498329745

message = '%5.3f' %(decnum)
print(message)

message = '%7.2f' %(decnum)
print(message)

# first time message would read 1.725 with no space because that would make total spaces used 5(decimal is included in the space)
# second message would read 3 space in and 1.72 that would make total spaces 7

# Question 5

# from http.client import NON_AUTHORITATIVE_INFORMATION


p, q = 111, 13

result = p/q

message = 'The result of %d divided by %d is %.3f, correct to 3 decimal places'%(p,q,result)
print(message)

# it prints as "The result of 111 divided by 13 is 8.538, correct to 3 decimal places"

# Question 6

message = 'My name is {} and I am {} years old.'.format('Jamie', 31)
print(message)

# prints as :  My name is Jamie and I am 31 years old

# Question 7

message1 = 'My favorite colors are {}, {} and {}.'.format('orange', 'blue', 'black')
message2 = 'My favorite colors are {1}, {0} and {2}.'.format('orange', 'blue', 'black')

print(message1)
print(message2)

# message1 prints as My favorite colors are orange, blue and black.
# message2 prints as My favorite colors are blue, orange and black.

student1 = 'Aaron'
student2 = 'Beck'
student3 = 'Carol'

# use three variables and format method 

message = 'My best friends are {}, {} and {}'.format(student1, student2, student3)
print(message)

# prints as My best friends are Aaron, Beck and Carol

message1 = '{:7.2f} and {:d}'.format(21.3124, 12)

message2 = '{1} and {0}'.format(21.3124, 12)

print(message1)
print(message2)

# prints out as     21.32 and 12
# prints out as 12 and 21.3124

# Question 10

x,y = 12, 7

quotient = x/y

# use format()

message = 'The result of {} divided by {} is {:.4f}, correct to 4 decimal places'.format(x,y,quotient)
print(message)

# Should print out 'The result of 12 divided by 7 is 1.7143, correct to 4 decimal places

# Question 11



number = 2.7123
number = int(number)

# assigns value 2.7123 to variable called number. cast number into integer
# and assign back to number

# question 12

str(2.12431)

# convert number to string

# Question 13

userInput = '12'
userInput = int(userInput)
print(userInput)

# assign variable to string then to integer

# Question 14

mylist = [1,2,3,4,5,6]

print(mylist[1])
# should be 2
print(mylist[-2])
# should be 5

# index 6 is invalid because first number in list is 0 not 1 so number six would be 5 not 6
# indexes start with 0

# Question 15

testScores = [10,11,12,13]

print(testScores[3])
print(testScores[-1])

# output
# 13
# 13


# Question 16

myList = [1,2,3,4,5,6,7,8,9,10]
myList1 = myList
myList2 = myList[3:6]
myList3 = myList[:5]
myList4 = myList[2:]
myList5 = myList[1:7:2]
myList6 = myList[ : :3]

print(myList)
print(myList1)
print(myList2)
print(myList3)
print(myList4)
print(myList5)
print(myList6)

# prints out
# [1,2,3.4,5,6,7,8,9,10]
# [4,5,6]
# [1,2,3,4,5]
# [3,2,1]
# [2,4,6]
# [1,4,7,10]

# Question 17

q17 = [11,12,13,14,15,16,17,18,19,20]

# slice to select number 13 to 18 and assign to sliceA

sliceA = q17[2:8]

# slice to select 13, 16 and 19 and assign to sliceB

sliceB = q17[2:10:3]
# 
# answer from book
sliceB = q17[2: :3]


# print slice A and slice B

print(sliceA)
print(sliceB)

# Question 18

emptyList = []

emptyList.append(12)
emptyList.append(5)
emptyList.append(9)
emptyList.append(11)

print(emptyList)

# prints [12,5,9,11]

q19 = [1,2,3,4,5]

q19[2] = 10

print(q19)

# should print [1,2,10,4,5]

# question 20

q20 = ['A','B','C','D','E']

del q20[2]
del q20[0]

print(q20)
# should print ['B','D','E']
# remove C [2] before removing A[0] because positions change and could accidentally remove wrong item

# Question 21

daysofWeek = ('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')
myDay = daysofWeek[2]

print(myDay)

# assigned third element of daysOfWeek to myDay so assigned third element to myDay and printed. 
# output should be: Tues


# Question 22

# nameAgeDict = {'John':12, 'Matthew':15, 'Aaron':13, 'John':13, 'Melvin':10}

# in dictionary the names are key and numbers are value. can't have same key twice.
# 'John' is used as key twice
# for it to work better give one or both John's an initial

nameAgeDict = {'John':12, 'Matthew':15, 'Aaron':13, 'JohnB':13, 'Melvin':10}

# Question 23

dict1 = {'Aaron':11, 'Betty':5, 0: 'Zero', 3.9:'Three'}

print(dict1['Aaron'])
print(dict1[0])
print(dict1[3.9])
dict1['Aaron'] = 12
print(dict1)

del dict1['Betty']
print(dict1)

# expect output to be
# 11
# Zero
# Three
# { 'Aaron':12, 'Betty': 5, 0: 'Zero', 3.9: 'Three'}
# {'Aaron':12, 0:'Zero, 3.9: 'Three'}
# with dict it prints out keys and values

# Question 24

dict1 = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}

# dict1()
print(dict1['Four'])
dict1['Three'] = 3.1
del dict1['Two']
print(dict1)

# output
# 4
# {'One':1, 'Three':3.1, 'Four': 4, 'Five':5}

# Question 25

capitals = {'USA':'Washington D.C.', 'United Kingdom':'London', 'China': 'Beijing', 'Japan':'Tokyo', 'France':'Paris'}
print(capitals)

del capitals['China']
print(capitals)

capitals['Germany'] = 'Berlin'
capitals['Malaysia'] = 'Kuala Lumpur'

print(capitals)

# Output
# {'USA': 'Washington D.C.', 'United Kingdom': 'London', 'China': 'Beijing', 'Japan': 'Tokyo', 'France': 'Paris'}
# {'USA': 'Washington D.C.', 'United Kingdom': 'London', 'Japan': 'Tokyo', 'France': 'Paris'}
# {'USA': 'Washington D.C.', 'United Kingdom': 'London', 'Japan': 'Tokyo', 'France': 'Paris', 'Germany': 'Berlin', 'Malaysia': 'Kuala Lumpur'}

