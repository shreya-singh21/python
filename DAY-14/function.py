#Defining a function
# def myfun():
#     print('funtion is called')

#Calling a function
#myfun()


# def greeting(user_name,age=None):
#     print('*'*20)
#     print(f'welcome {user_name}')
#     print(f'age is {age}')
#     print('thank you for signing in')
#     print('*'*20)

# greeting('raju',25)
# greeting('sham',30)
# greeting('ram')

# def greeting(user_name,*hobbies):          #*hobbies - willl print list of hobbies
#     print('*'*20)
#     print(f'welcome {user_name}')
#     for hobby in hobbies:
#         print(f'Hobby is {hobby}')
#     print('thank you for signing in')
#     print('*'*20)

# greeting('raju','singing', 'dancing','shooting')
# greeting('sham','playing','swimming')
# greeting('ram','TV','football')


# def greeting(user_name,**user_info):  #dynamic argument - key,value
#     print('*'*20)
#     print(f'welcome {user_name}')
#     for key,value in user_info.items():
#         print(f'{key} is {value}')
#     print('thank you for signing in')
#     print('*'*20)

# greeting('raju',age=18, city='delhi',email='raju@gmail.com')
# greeting('sham',age=30, city='bhopal')
# greeting('ram')
    
def add(num1, num2):
    return num1+num2

#print(add(10,20))
result=add(10,20)
print(result)

