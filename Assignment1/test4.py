def check_number():
        global Secret_Number
        Secret_Number_list=list(Secret_Number)
        for i in range(3):
            if Secret_Number_list.count(Secret_Number[i])==1:
                return True
            else:
                return False
import random
Secret_Number=input('The number you want computer to guess:')
while True:
    Guess_Number_1=str(random.randint(100,999))
    if check_number():
        break
print('Guess 1:',Guess_Number_1)
Correct_Digits=input('How many correct digits?')
Exact_Digits=input('How many exact digits?')
Number_list_0=['0','1','2','3','4','5','6','7','8','9']
if Correct_Digits=='0':
    for i in range(3):
        Number_list_0.remove(Guess_Number_1[i])
    Number_list_1=random.sample(Number_list_0,3)
    Guess_Number_2=''.join(Number_list_1)
    print('Guess 2:',Guess_Number_2)
    Correct_Digits=input('How many correct digits?')
    Exact_Digits=input('How many exact digits?')
    if Correct_Digits=='0':
        for i in range(3):
            Number_list_1.remove(Guess_Number_2[i])
        Number_list_2=random.sample(Number_list_1,3)
        Guess_Number_3=''.join(Number_list_2)
        print('Guess 3:',Guess_Number_3)
        Correct_Digits=input('How many correct digits?')
        Exact_Digits=input('How many exact digits?')
        if Correct_Digits=='2':
            Number_list_3=list()
            for i in range(3):
                Number_list_3.append(Guess_Number_3[i])
            for i in range(3):
                Number_list_2.remove(Guess_Number_3[i])
            Number_list_4=Number_list_3
            Number_list_4[0]=Number_list_2[0]
            Guess_Number_4=''.join(Number_list_4)
            print('Guess 4:',Guess_Number_4)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='2':
                Number_list_4=Number_list_3
                Number_list_4[1]=Number_list_2[0]
                Guess_Number_5=''.join(Number_list_4)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='2':
                    Number_list_4=Number_list_3
                    Number_list_4[2]=Number_list_2[0]
                    Guess_Number_6=''.join(Number_list_4)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="0":
                        Number_list_4.insert(2,Number_list_4[0])
                        del Number_list_4[3]
                        Guess_Number_7=''.join(Number_list_4)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Exact_Digits=="0":
                            Number_list_4.insert(2,Number_list_4[0])
                            del Number_list_4[3]
                            Guess_Number_8=''.join(Number_list_4)
                            print('Guess 8:',Guess_Number_7)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!',Guess_Number_8)
                        elif Exact_Digits=='3':
                            print('Yes!It is the Number!',Guess_Number_7)
                    elif Exact_Digits=='1':
                        Number_list_4.insert(1,Number_list_4[2])
                        del Number_list_4[3]
                        Guess_Number_7=''.join(Number_list_4)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Exact_Digits=="1":
                            Number_list_4.insert(0,Number_list_4[2])
                            del Number_list_4[3]
                            Guess_Number_8=''.join(Number_list_4)
                            print('Guess 8:',Guess_Number_8)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            if Exact_Digits=="1":
                                Number_list_4.insert(0,Number_list_4[1])
                                del Number_list_4[2]
                                Guess_Number_9=''.join(Number_list_4)
                                print('Guess 9:',Guess_Number_9)
                                Correct_Digits=input('How many correct digits?')
                                Exact_Digits=input('How many exact digits?')
                                print('Yes!It is the Number!',Guess_Number_9)
                            else:
                                print('Yes!It is the Number!',Guess_Number_8)
                        else:
                            print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                elif Correct_Digits=='3' and Exact_Digits=='0':
                    Number_list_4.insert(2,Number_list_4[0])
                    del Number_list_4[3]
                    Guess_Number_6=''.join(Number_list_4)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="0":
                        Number_list_4.insert(2,Number_list_4[0])
                        del Number_list_4[3]
                        Guess_Number_7=''.join(Number_list_4)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!',Guess_Number_7)
                    elif Exact_Digits=='3':
                        print('Yes!It is the Number!',Guess_Number_6)
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Number_list_4.insert(1,Number_list_4[2])
                    del Number_list_4[3]
                    Guess_Number_6=''.join(Number_list_4)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="1":
                        Number_list_4.insert(0,Number_list_4[2])
                        del Number_list_4[3]
                        Guess_Number_7=''.join(Number_list_4)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Exact_Digits=="1":
                            Number_list_4.insert(0,Number_list_4[1])
                            del Number_list_4[2]
                            Guess_Number_8=''.join(Number_list_4)
                            print('Guess 8:',Guess_Number_8)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!',Guess_Number_8)
                        else:
                            print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
            elif Correct_Digits=='3' and Exact_Digits=='0':
                Number_list_4.insert(2,Number_list_4[0])
                del Number_list_4[3]
                Guess_Number_5=''.join(Number_list_4)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Exact_Digits=="0":
                    Number_list_4.insert(2,Number_list_4[0])
                    del Number_list_4[3]
                    Guess_Number_6=''.join(Number_list_4)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!',Guess_Number_6)
                elif Exact_Digits=='3':
                    print('Yes!It is the Number!',Guess_Number_5)
            elif Correct_Digits=='3' and Exact_Digits=='1':
                Number_list_4.insert(1,Number_list_4[2])
                del Number_list_4[3]
                Guess_Number_5=''.join(Number_list_4)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Exact_Digits=="1":
                    Number_list_4.insert(0,Number_list_4[2])
                    del Number_list_4[3]
                    Guess_Number_6=''.join(Number_list_4)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="1":
                        Number_list_4.insert(0,Number_list_4[1])
                        del Number_list_4[2]
                        Guess_Number_7=''.join(Number_list_4)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
            else:
                print('Yes!It is the number!',Guess_Number_4)
        elif Correct_Digits=='3' and Exact_Digits=='0':
            Number_list_2.insert(2,Number_list_2[0])
            del Number_list_2[3]
            Guess_Number_4=''.join(Number_list_2)
            print('Guess 4:',Guess_Number_4)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Exact_Digits=="0":
                Number_list_2.insert(2,Number_list_2[0])
                del Number_list_2[3]
                Guess_Number_5=''.join(Number_list_2)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                print('Yes!It is the Number!',Guess_Number_5)
            elif Exact_Digits=='3':
                print('Yes!It is the Number!',Guess_Number_4)
        elif Correct_Digits=='3' and Exact_Digits=='1':
            Number_list_2.insert(1,Number_list_2[2])
            del Number_list_2[3]
            Guess_Number_4=''.join(Number_list_2)
            print('Guess 4:',Guess_Number_4)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Exact_Digits=="1":
                Number_list_2.insert(0,Number_list_2[2])
                del Number_list_2[3]
                Guess_Number_5=''.join(Number_list_2)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Exact_Digits=="1":
                    Number_list_2.insert(0,Number_list_2[1])
                    del Number_list_2[2]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
            else:
                print('Yes!It is the Number!',Guess_Number_4)
        else:
            print('Yes!It is the number!',Guess_Number_3)
    if Correct_Digits=='1':
        Number_list_2=list()
        for i in range(3):
            Number_list_0.remove(Guess_Number_2[i])
            Number_list_2.append(Guess_Number_2[i])
        Guess_Number_3=Number_list_0[0]+Number_list_0[1]+Number_list_2[0]
        print('Guess 3:',Guess_Number_3)
        Correct_Digits=input('How many correct digits?')
        Exact_Digits=input('How many exact digits?')
        if Correct_Digits=='0':
            Guess_Number_4=Number_list_0[0]+Number_list_0[1]+Number_list_2[1]
            print('Guess 4:',Guess_Number_4)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='0':
                Guess_Number_5=Number_list_0[2]+Number_list_0[3]+Number_list_2[2]
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Number_list_2=list()
                    for i in range(3):
                        Number_list_2.append(Guess_Number_5[i])
                    Number_list_2.insert(2,Number_list_2[0])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="0":
                        Number_list_2.insert(2,Number_list_2[0])
                        del Number_list_2[3]
                        Guess_Number_7=''.join(Number_list_2)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!',Guess_Number_7)
                    elif Exact_Digits=='3':
                        print('Yes!It is the Number!',Guess_Number_6)
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Number_list_2=list()
                    for i in range(3):
                        Number_list_2.append(Guess_Number_5[i])
                    Number_list_2.insert(1,Number_list_2[2])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="1":
                        Number_list_2.insert(0,Number_list_2[2])
                        del Number_list_2[3]
                        Guess_Number_7=''.join(Number_list_2)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Exact_Digits=="1":
                            Number_list_2.insert(0,Number_list_2[1])
                            del Number_list_2[2]
                            Guess_Number_8=''.join(Number_list_2)
                            print('Guess 8:',Guess_Number_8)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!',Guess_Number_8)
                        else:
                            print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
            elif Correct_Digits=='1':
                Guess_Number_5=Number_list_0[2]+Number_list_0[3]+Number_list_2[1]
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Correct_Digits=='3' and Exact_Digits=='0':
                    Number_list_2=list()
                    for i in range(3):
                        Number_list_2.append(Guess_Number_5[i])
                    Number_list_2.insert(2,Number_list_2[0])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="0":
                        Number_list_2.insert(2,Number_list_2[0])
                        del Number_list_2[3]
                        Guess_Number_7=''.join(Number_list_2)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!',Guess_Number_7)
                    elif Exact_Digits=='3':
                        print('Yes!It is the Number!',Guess_Number_6)
                elif Correct_Digits=='3' and Exact_Digits=='1':
                    Number_list_2=list()
                    for i in range(3):
                        Number_list_2.append(Guess_Number_5[i])
                    Number_list_2.insert(1,Number_list_2[2])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="1":
                        Number_list_2.insert(0,Number_list_2[2])
                        del Number_list_2[3]
                        Guess_Number_7=''.join(Number_list_2)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        if Exact_Digits=="1":
                            Number_list_2.insert(0,Number_list_2[1])
                            del Number_list_2[2]
                            Guess_Number_8=''.join(Number_list_2)
                            print('Guess 8:',Guess_Number_8)
                            Correct_Digits=input('How many correct digits?')
                            Exact_Digits=input('How many exact digits?')
                            print('Yes!It is the Number!',Guess_Number_8)
                        else:
                            print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
        elif Correct_Digits=='1':
            Guess_Number_4=Number_list_0[2]+Number_list_0[3]+Number_list_2[0]
            print('Guess 4:',Guess_Number_4)
            Correct_Digits=input('How many correct digits?')
            Exact_Digits=input('How many exact digits?')
            if Correct_Digits=='3' and Exact_Digits=='0':
                Number_list_2=list()
                for i in range(3):
                    Number_list_2.append(Guess_Number_5[i])
                Number_list_2.insert(2,Number_list_2[0])
                del Number_list_2[3]
                Guess_Number_5=''.join(Number_list_2)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Exact_Digits=="0":
                    Number_list_2.insert(2,Number_list_2[0])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    print('Yes!It is the Number!',Guess_Number_6)
                elif Exact_Digits=='3':
                    print('Yes!It is the Number!',Guess_Number_5)
            elif Correct_Digits=='3' and Exact_Digits=='1':
                Number_list_2=list()
                for i in range(3):
                    Number_list_2.append(Guess_Number_5[i])
                Number_list_2.insert(1,Number_list_2[2])
                del Number_list_2[3]
                Guess_Number_5=''.join(Number_list_2)
                print('Guess 5:',Guess_Number_5)
                Correct_Digits=input('How many correct digits?')
                Exact_Digits=input('How many exact digits?')
                if Exact_Digits=="1":
                    Number_list_2.insert(0,Number_list_2[2])
                    del Number_list_2[3]
                    Guess_Number_6=''.join(Number_list_2)
                    print('Guess 6:',Guess_Number_6)
                    Correct_Digits=input('How many correct digits?')
                    Exact_Digits=input('How many exact digits?')
                    if Exact_Digits=="1":
                        Number_list_2.insert(0,Number_list_2[1])
                        del Number_list_2[2]
                        Guess_Number_7=''.join(Number_list_2)
                        print('Guess 7:',Guess_Number_7)
                        Correct_Digits=input('How many correct digits?')
                        Exact_Digits=input('How many exact digits?')
                        print('Yes!It is the Number!',Guess_Number_7)
                    else:
                        print('Yes!It is the Number!',Guess_Number_6)
                else:
                    print('Yes!It is the Number!',Guess_Number_5)
            else:
                print('Yes!It is the Number!',Guess_Number_4)



