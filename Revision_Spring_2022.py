#First Question
continues = 'Y'
while continues=='Y':
    A1 = input('insert array1: ').split()
    A2 = input('insert array2: ').split()
    #A1 = [int(x) for x in A1] not required to convert into integers
    found_occurances = 0   #sum
    locations = []
    for i in range(len(A1)-1):   # to bypass the out of range error
        if A2[0]==A1[i] and A2[1] == A1[i+1]:
            found_occurances = found_occurances + 1 #found_occurances +=1
            locations.append(i)
    if found_occurances != 0:
        #print('%-10s%-10s%'% ('A','A',''))
        #print(f'alalajbfjdjdfjdfjdkj {continues} dgsdhegfdejhfgerhjgfhgf')
        print('The pattern is found',found_occurances, 'time(s)')        #print(x,y,z)   12 34 78  
        print(f'the pattern is found{found_occurances}time(s) at the following positions:')
        print(locations)
    else: 
        print('pattern not found')

    continues = input('Do you wish to continue? <Y/N>')
    while continues != 'Y' and continues != 'N':   # error check
        continues = input('Error ya toxic! Do you wish to continue? <Y/N>')
print('Good Bye ya TOXIC')

# changes = 0
# number_correct = 0
# number_incorrect = 0
# v = input('Enter a vector').split()
# while len(v) != 1:  #Did not mention the empty array case
#     correct = False
#     for i in range(len(v)-1):
#         if int(v[i])*int(v[i+1]) < 0:
#             changes = changes+1
#             correct = True
#     if correct == True:
#         number_correct = number_correct +1
#         v = input('Enter a vector').split()
#     else: 
#         number_incorrect = number_incorrect + 1
#         v = input('No sign changes are found! Reenter the vector:').split()
# print(f'You have entered {number_correct} correct sequence(s) with {changes} sign changes total\nGood Bye!')

