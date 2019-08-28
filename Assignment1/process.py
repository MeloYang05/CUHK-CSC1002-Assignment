def check_number():
        global Secret_Number
        Guess_Number_list=list(Guess_Number)
        for i in range(3):
            if Guess_Number_list.count(Guess_Number[i])==1:
                return True
            else:
                return False
import random
Secret_Number=input('The number you want computer to guess:')
while True:
    Guess_Number=str(random.randint(100,999))
    if check_number():
        break
print('Guess:',Guess_Number)
Correct_Digits=input('How many correct digits?')
Exact_Digits=input('How many exact digits?')
Number_list_0=['9','8','7','6','5','4','3','2','1','0']
if Correct_Digits=='0':
    for i in range(3):
        Number_list_0.remove(Guess_Number[i])
    Guess_Number=Number_list_0[0]+Number_list_0[1]+Number_list_0[2]
    print('Guess:',Guess_Number)
    Correct_Digits=input('How many correct digits?')
    Exact_Digits=input('How many exact digits?')
    if Correct_Digits=='0':
        for i in range(3):
            Number_list_0.remove(Guess_Number[i])
        Guess_Number=Number_list_0[0]+Number_list_0[1]+Number_list_0[2]
        print('Guess:',Guess_Number)
        Correct_Digits=input('How many correct digits?')
        Exact_Digits=input('How many exact digits?')
        if Correct_Digits=='2':
            Number_list_1=list()
            for i in range(3):
                Number_list_1.append(Guess_Number[i])
            for i in range(3):
                Number_list_0.remove(Guess_Number[i])
            Guess_Number=Number_list_0[0]+Number_list_1[0]+Number_list_1[1]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='2' and Exact_Digits=='0': 
                Guess_Number=Number_list_1[0]+Number_list_0[0]+Number_list_1[2]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='2' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[1]+Number_list_1[2]+Number_list_0[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='1':
                        Guess_Number=Number_list_1[2]+Number_list_1[1]+Number_list_0[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='2' and Exact_Digits=='2':
                    Guess_Number=Number_list_1[1]+Number_list_0[0]+Number_list_0[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                elif Correct_Digits=='3'and Exact_Digits=='1':
                    Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_1[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_1[0]+Number_list_1[2]+Number_list_0[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='2' and Exact_Digits=='1':
                Guess_Number=Number_list_0[0]+Number_list_1[2]+Number_list_1[0]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[2]+Number_list_1[0]+Number_list_0[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                elif Correct_Digits=='2' and Exact_Digits=='1':
                    Guess_Number=Number_list_0[0]+Number_list_1[1]+Number_list_1[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes! It is the Number!')
                elif Correct_Digits=='2' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_1[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes! It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='2' and Exact_Digits=='2':
                Guess_Number=Number_list_0[0]+Number_list_1[0]+Number_list_1[2]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='2' and Exact_Digits=='1':
                    Guess_Number=Number_list_0[0]+Number_list_1[2]+Number_list_1[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='0':
                Guess_Number=Number_list_1[0]+Number_list_1[1]+Number_list_0[0]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[1]+Number_list_0[0]+Number_list_1[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='1':
                Guess_Number=Number_list_1[0]+Number_list_0[0]+Number_list_1[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[1]+Number_list_1[0]+Number_list_0[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[0]+Number_list_1[1]+Number_list_1[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
        elif Correct_Digits=='3' and Exact_Digits=='0':
            Guess_Number=Number_list_0[1]+Number_list_0[2]+Number_list_0[0]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='3' and Exact_Digits=='0':
                Guess_Number=Number_list_0[2]+Number_list_0[0]+Number_list_0[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                print('Yes!It is the Number!')
            else:
                print('Yes!It is the Number!')
        elif Correct_Digits=='3' and Exact_Digits=='1':
            Guess_Number=Number_list_0[1]+Number_list_0[0]+Number_list_0[2]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='3' and Exact_Digits=='0':
                Guess_Number=Number_list_0[2]+Number_list_0[1]+Number_list_0[0]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[0]+Number_list_0[2]+Number_list_0[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            else:
                print('Yes!It is the Number!')
        else:
            print('Yes!It is the Number!')
    elif Correct_Digits=='1':
        Number_list_1=list()
        for i in range(3):
            Number_list_0.remove(Guess_Number[i])
            Number_list_1.append(Guess_Number[i])
        Guess_Number=Number_list_1[0]+Number_list_0[0]+Number_list_0[1]
        print('Guess:',Guess_Number)
        Correct_Digits=input('How many correct digits?')
        Exact_Digits=input('How many exact digits?')
        if Correct_Digits=='0':
            Guess_Number=Number_list_1[1]+Number_list_0[2]+Number_list_0[3]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='2' and Exact_Digits=='0':
                Guess_Number=Number_list_0[2]+Number_list_0[3]+Number_list_1[2]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[3]+Number_list_1[2]+Number_list_0[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='2' and Exact_Digits=='1':
                Guess_Number=Number_list_0[3]+Number_list_0[2]+Number_list_1[2]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[2]+Number_list_1[2]+Number_list_0[3]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='2' and Exact_Digits=='2':
                Guess_Number=Number_list_1[2]+Number_list_0[2]+Number_list_0[3]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='0':
                Guess_Number=Number_list_0[2]+Number_list_0[3]+Number_list_1[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[3]+Number_list_1[1]+Number_list_0[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='1':
                Guess_Number=Number_list_0[2]+Number_list_1[1]+Number_list_0[3]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[3]+Number_list_0[2]+Number_list_1[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_1[1]+Number_list_0[3]+Number_list_0[2]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            else:
                print('Yes!It is the Number!')
        elif Correct_Digits=='1':
            Guess_Number=Number_list_1[1]+Number_list_0[0]+Number_list_0[1]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='0':
                Guess_Number=Number_list_1[0]+Number_list_0[2]+Number_list_0[3]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[2]+Number_list_0[3]+Number_list_1[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[3]+Number_list_1[0]+Number_list_0[2]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Guess_Number=Number_list_0[2]+Number_list_1[0]+Number_list_0[3]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[3]+Number_list_0[2]+Number_list_1[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_1[0]+Number_list_0[3]+Number_list_0[2]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='1':
                Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_0[2]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='1':
                    Guess_Number=Number_list_1[2]+Number_list_0[1]+Number_list_0[3]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_1[2]+Number_list_0[1]+Number_list_0[3]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_0[3]+Number_list_1[2]+Number_list_0[1]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    elif Correct_Digits=='3' and Exact_Digits=='1':
                        Guess_Number=Number_list_0[1]+Number_list_1[2]+Number_list_0[3]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_0[3]+Number_list_0[1]+Number_list_1[2]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            if Correct_Digits=='3' and Exact_Digits=='0':
                                Guess_Number=Number_list_1[2]+Number_list_0[3]+Number_list_0[1]
                                print('Guess:',Guess_Number)
                                Correct_Digits=input('How many correct digits?')
                                Exact_Digits=input('How many exact digits?')
                                print('Yes!It is the Number!')
                            else:
                                print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='2':
                    Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_0[3]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='1':
                        Guess_Number=Number_list_1[2]+Number_list_0[2]+Number_list_0[1]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_0[2]+Number_list_0[1]+Number_list_1[2]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            if Correct_Digits=='3' and Exact_Digits=='0':
                                Guess_Number=Number_list_0[1]+Number_list_1[2]+Number_list_0[2]
                                print('Guess:',Guess_Number)
                                Correct_Digits=input('How many correct digits?')
                                Exact_Digits=input('How many exact digits?')
                                print('Yes!It is the Number!')
                            else:
                                print('Yes!It is the Number!')
                        elif Correct_Digits=='3' and Exact_Digits=='1':
                            Guess_Number=Number_list_0[2]+Number_list_1[2]+Number_list_0[1]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            if Correct_Digits=='3' and Exact_Digits=='0':
                                Guess_Number=Number_list_0[1]+Number_list_0[2]+Number_list_1[2]
                                print('Guess:',Guess_Number)
                                Correct_Digits=input('How many correct digits?')
                                Exact_Digits=input('How many exact digits?')
                                if Correct_Digits=='3' and Exact_Digits=='0':
                                    Guess_Number=Number_list_1[2]+Number_list_0[1]+Number_list_0[2]
                                    print('Guess:',Guess_Number)
                                    Correct_Digits=input('How many correct digits?')
                                    Exact_Digits=input('How many exact digits?')
                                    print('Yes!It is the Number!')
                                else:
                                    print('Yes!It is the Number!')
                            else:
                                print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    elif Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[0]+Number_list_0[3]+Number_list_1[2]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_0[3]+Number_list_1[2]+Number_list_0[0]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    elif Correct_Digits=='3' and Exact_Digits=='1':
                        Guess_Number=Number_list_0[0]+Number_list_1[2]+Number_list_0[3]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_0[3]+Number_list_0[0]+Number_list_1[2]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            if Correct_Digits=='3' and Exact_Digits=='0':
                                Guess_Number=Number_list_1[2]+Number_list_0[3]+Number_list_0[0]
                                print('Guess:',Guess_Number)
                                Correct_Digits=input('How many correct digits?')
                                Exact_Digits=input('How many exact digits?')
                                print('Yes!It is the Number!')
                            else:
                                print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[0]+Number_list_0[2]+Number_list_1[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[2]+Number_list_1[2]+Number_list_0[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Guess_Number=Number_list_0[0]+Number_list_1[2]+Number_list_0[2]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[2]+Number_list_0[0]+Number_list_1[2]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_1[2]+Number_list_0[2]+Number_list_0[0]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
        elif Correct_Digits=='2':
            Guess_Number=Number_list_1[1]+Number_list_0[0]+Number_list_0[1]
            print('Guess:',Guess_Number)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='2':
                Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_0[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_1[2]+Number_list_0[0]+Number_list_0[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[1]+Number_list_1[2]+Number_list_0[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Guess_Number=Number_list_0[20]+Number_list_1[2]+Number_list_0[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_0[1]+Number_list_0[0]+Number_list_1[2]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Correct_Digits=='3' and Exact_Digits=='0':
                            Guess_Number=Number_list_1[2]+Number_list_0[1]+Number_list_0[0]
                            print('Guess:',Guess_Number)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!')
                        else:
                            print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')            
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='0':
                Guess_Number=Number_list_0[0]+Number_list_0[1]+Number_list_1[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[1]+Number_list_1[1]+Number_list_0[0]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            elif Correct_Digits=='3' and Exact_Digits=='1':
                Guess_Number=Number_list_0[0]+Number_list_1[1]+Number_list_0[1]
                print('Guess:',Guess_Number)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Guess_Number=Number_list_0[1]+Number_list_0[0]+Number_list_1[1]
                    print('Guess:',Guess_Number)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Correct_Digits=='3' and Exact_Digits=='0':
                        Guess_Number=Number_list_1[1]+Number_list_0[1]+Number_list_0[0]
                        print('Guess:',Guess_Number)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!')
                    else:
                        print('Yes!It is the Number!')
                else:
                    print('Yes!It is the Number!')
            else:
                print('Yes!It is the Number!')
        
