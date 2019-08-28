def check_number():
        global Correct_number
        Correct_number_list=list(Correct_number)
        global Correct_number_length
        for i in range(eval(Correct_number_length)):
            if Correct_number_list.count(Correct_number[i])==1:
                return True
            else:
                return False
import random
while True:
    Correct_number_length=input('Please enter the length of the number,3 or 4:')
    if Correct_number_length=='3':
        while True:
            Correct_number= str(random.randint(100,999))
            if check_number():
                print('The random number has been made up successfully, please guess now')
                break
        break
    elif Correct_number_length=='4':
        while True:
            Correct_number= str(random.randint(1000,9999))
            if check_number():
                print('The random number has been made up successfully, please guess now')
                break
        break
    else:
        print('Wrong input, please try again')
print(Correct_number)
if Correct_number_length=='3':
    output_list=list()
    for h in range(1,16):
        print()
        Guess_number=input('Guess '+str(h)+'/15:')
        count_exact=0
        count_number=0
        for i in range(3):
            if Guess_number[i]==Correct_number[i]:
                count_exact=count_exact+1
        for j in range(3):
            if Guess_number[j] in Correct_number:
                count_number=count_number+1
        print('How many correct digits?',count_number)
        print('How many exact digits?',count_exact,'\n')
        output_list.append('Guess '+str(h)+'/15:'+str(Guess_number)+' Correct='+str(count_number)+' Exact='+str(count_exact))
        for k in range(h):
            print(output_list[k])
        if count_number==3:
            replay=input('Congratulations!!Do you want to play it again? y/n:')
            if replay=='n':
                break