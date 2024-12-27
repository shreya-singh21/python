#ordered sequence of diffrent types of values

#How to define a list?
#users=['raju','sham','paul']

#how to get values from list?
#users[0]
#users[1]
#users[2]

user_list=['alex','raju','sham','ram']
print(user_list)
print(user_list[0])

#Adding item to list
user_list.append('paul')
print(user_list)

#How to delete values from list
user_list.remove('raju')
print(user_list)

#Insert at particular index
user_list.insert(1,'shanu')
print(user_list)

#How to delete values from list using index number
del user_list[3]
print(user_list)

#Length of list
print(len(user_list))

#sorting of list
user_list.sort()
print(user_list)

#slicing of list
print(user_list[0:3]) #will print 0 1 2

#Numeric list
marks=[89,90,100,67,85]
print(marks)

#minimum marks
print(min(marks))

#maximum marks
print(max(marks))

#sum marks
print(sum(marks))