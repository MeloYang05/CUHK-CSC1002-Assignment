import random
import os
Number_list=list()
output_list=list()
def check_number(a):
    a_list=list(a)
    count=0
    for i in range(3):
        if a_list.count(a[i])==1:
            count=count+1
    if count==3:
        return True
    else:
        return False

def combine(m,n,i):
    global Guess_Number
    if Guess_Number[m]==i[m] and Guess_Number[n]==i[n]:
        return True
    else:
        return False

def check_intersection_1():
    global Number_list
    global Guess_Number
    Number_list_0=list()
    for h in Number_list:
        set1=set(Guess_Number)
        set2=set(h)
        set3=set1&set2
        list1=list(set3)
        c=len(list1)
        if c==eval(Correct_Digits):
            Number_list_0.append(h)
    if len(Number_list_0)==0:
        print('Your input must be wrong, please try again!')
        os._exit(0)
    else:
        Number_list=Number_list_0

def check_intersection_2():
    global Number_list
    global Guess_Number
    global Exact_Digits
    Number_list_0=list()
    if Exact_Digits=='1':
        for i in Number_list:
            if Guess_Number[0]==i[0] or Guess_Number[1]==i[1] or Guess_Number[2]==i[2]: 
                Number_list_0.append(i)
        if len(Number_list_0)==0:
            print('Your input must be wrong, please try again!')
            os._exit(0)
        else:
            Number_list=Number_list_0
    elif Exact_Digits=='2':
        for i in Number_list:
            if combine(0,1,i) or combine(0,2,i) or combine(1,2,i):
                Number_list_0.append(i)
        if len(Number_list_0)==0:
            print('Your input must be wrong, please try again!')
            os._exit(0)
        else:
            Number_list=Number_list_0

while True:
    for j in range(100,999):
        j=str(j)
        if check_number(j):
            Number_list.append(j)
    print('Welcome! This program allows the computer to guess triple digits')
    while True:
        Secret_Number=input('The number without repeated digits you want computer to guess(The computer will not know it now):')
        if Secret_Number.isdigit() and len(Secret_Number)==3 and check_number(Secret_Number):
            break
        else:
            print('Your input is wrong! Please try again!')
    count=0
    while True:
        count=count+1
        Guess_Number=''.join(random.sample(Number_list,1))
        print('Guess ',count,' : ',Guess_Number,sep='')
        while True:
            Correct_Digits=input('How many correct digits?')
            if not Correct_Digits=='0':
                Exact_Digits=input('How many exact digits?')
                print()
            else:
                Exact_Digits='0'
                print()
            if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                break
            else:
                print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')
        count_str=str(count)
        output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
        output_list.append(output_record)
        for l in output_list:
            print(l)
        print()
        check_intersection_1()
        check_intersection_2()
        if Correct_Digits=='3':
            break
    if Exact_Digits=='0':
        count=count+1
        Guess_Number=Guess_Number[1]+Guess_Number[2]+Guess_Number[0]
        print('Guess ',count,' : ',Guess_Number,sep='')
        while True:    
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            print()
            if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                break
            else:
                print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')        
        count_str=str(count)
        output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
        output_list.append(output_record)
        for l in output_list:
            print(l)
        print()    
        if Exact_Digits=='0' and Correct_Digits=='3':
            count=count+1
            Guess_Number=Guess_Number[1]+Guess_Number[2]+Guess_Number[0]
            print('Guess ',count,' : ',Guess_Number,sep='')
            while True:
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                print()
                if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                    break
                else:
                    print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')
            count_str=str(count)
            output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
            output_list.append(output_record)
            for l in output_list:
                print(l)
            print()
            print('Yes!It is the Number!')
            button= input('Do you want to play again? Y/N:')
            if button=='N':
                break
            elif button=='Y':
                continue
            else:
                print('Your input is wrong. Program closes automatically.')
        elif not Exact_Digits=='0' and  not Exact_Digits=='3'  or not Correct_Digits=='3':
            print('Your input must be wrong! Please try again!')
            os._exit(0)
        else:
            print('Yes!It is the Number!')
    elif Exact_Digits=='1':
        count=count+1
        Guess_Number=Guess_Number[1]+Guess_Number[0]+Guess_Number[2]
        print('Guess ',count,' : ',Guess_Number,sep='')
        while True:
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            print()
            if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                break
            else:
                print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')
        count_str=str(count)
        output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
        output_list.append(output_record)
        for l in output_list:
            print(l)
        print()
        if not Exact_Digits=='3' and Correct_Digits=='3':
            count=count+1
            Guess_Number=Guess_Number[1]+Guess_Number[0]+Guess_Number[2]
            Guess_Number=Guess_Number[2]+Guess_Number[1]+Guess_Number[0]
            print('Guess ',count,' : ',Guess_Number,sep='')
            while True:
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                print()
                if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                    break
                else:
                    print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')
            count_str=str(count)
            output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
            output_list.append(output_record)
            for l in output_list:
                print(l)
            print()
            if not Exact_Digits=='3' and Correct_Digits=='3':
                count=count+1
                Guess_Number=Guess_Number[2]+Guess_Number[1]+Guess_Number[0]
                Guess_Number=Guess_Number[0]+Guess_Number[2]+Guess_Number[1]
                print('Guess ',count,' : ',Guess_Number,sep='')
                while True:
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print()
                    if 0<=eval(Correct_Digits)<=3 and Correct_Digits.isdigit() and Exact_Digits.isdigit() and eval(Exact_Digits)<=eval(Correct_Digits):
                        break
                    else:
                        print('Your input is wrong, please enter again! \nNote that both correct and exact digits should be integers.\nBoth >=0 and <=0.\nExact digits should <= Correct digits')
                count_str=str(count)
                output_record="Guess "+count_str+" : "+Guess_Number+' Correct: '+Correct_Digits+' Exact: '+Exact_Digits
                output_list.append(output_record)
                for l in output_list:
                    print(l)
                print()
                print('Yes!It is the Number!')
                button= input('Do you want to play again? Y/N:')
                if button=='N':
                    break
                elif button=='Y':
                    continue
                else:
                    print('Your input is wrong. Program closes automatically.')
            elif not Exact_Digits=='3' and not Exact_Digits=='0' or not Correct_Digits=='3':
                print('Your input must be wrong! Please try again!')
                os._exit(0)
            else:
                print('Yes!It is the Number!')
                button= input('Do you want to play again? Y/N:')
                if button=='N':
                    break
                elif button=='Y':
                    continue
                else:
                    print('Your input is wrong. Program closes automatically.')
        elif not Exact_Digits=='3' and not Exact_Digits=='0' or not Correct_Digits=='3':
            print('Your input must be wrong! Please try again!')
            os._exit(0)
        else:
            print('Yes!It is the Number!')
            button= input('Do you want to play again? Y/N:')
            if button=='N':
                break
            elif button=='Y':
                continue
            else:
                print('Your input is wrong. Program closes automatically.')
    else:
        print('Yes!It is the Number!')
        button= input('Do you want to play again? Y/N:')
        if button=='N':
            break
        elif button=='Y':
            continue
        else:
            print('Your input is wrong. Program closes automatically.')