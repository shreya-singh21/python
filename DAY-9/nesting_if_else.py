age=20
voter_id=False

if age>=18:
    if voter_id:
        print('yes you can vote')
    else:
        print('apply for voter id')
else:
    print('you cannot vote')

#AND Operator
if age>=18 and voter_id:
    print('You can vote')
else:
    print('you cannot vote')

#OR Operator
if age>=18 or voter_id:
     print('You can vote')
else:
    print('you cannot vote')