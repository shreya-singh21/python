#break - to stop the loop
#continue - to stop current iteration of loop and start next iteration

num = [10, -20, 30, -40, 50, -60, 70, -80]
for n in num:
    if n == 30:
         break
    print(n)

for n in num: 
    if n == 30:
        continue
    print(n)