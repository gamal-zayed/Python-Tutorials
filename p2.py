changes_total = 0
number_correct = 0
v = input('Enter a vector').split()
#v = [int(x) for x  in v]
while len(v) != 1:  #Did not mention the empty array case
    correct = False
    changes_particular = 0
    for i in range(len(v)-1):
        if int(v[i])*int(v[i+1]) < 0:
        #if (int(v[i])>0 and int(v[i+1])<0) or (int(v[i])<0 and int(v[i+1])>0):     
            changes_particular = changes_particular+1
            changes_total = changes_total  + 1
            correct = True
    if correct == True:
        number_correct = number_correct +1
        print(f'{changes_particular} sign changes were found')
        v = input('Enter a vector').split()
    else: 
        
    # while correct == False:
    #     v = input('No sign changes are found! Reenter the vector:').split()
        print(f'You have entered {number_correct} correct sequence(s) with {changes_total} sign changes total\nGood Bye!')


x = [1,2,3,4,5,6]
L = []
for i in range(len(x)-1, -1, -1):
    L.append(x[i])


for i in range(len(x)):
    L.append(x[len(x)-i-1])









#main
from Revision_Spring_2022 import toxic
n, e = toxic(3,6)
print(n)





def dist_calc(L,P):
    import math
    lengths = []
    for btngana in L:
        lengths.append(math.sqrt((btngana.values()[0]-P.values()[0])**2+ (btngana.values()[1]- P.values()[1])**2))
    return lengths    #list of distances between each point in L and P