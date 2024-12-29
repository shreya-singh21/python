print('Fizz Buzz Program')
till_num=int(input('Enter the specified number:'))
my_list=[]

for num in range(1,till_num+1):
    result=""
    if num%3==0:
        result=result+'fizz'
        if num%5==0:
            result=result+'buzz'
    elif num%5==0:
        result=result+'buzz'
    else:
        result=num

    #print(num)
    my_list.append(result)

print(my_list)
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
