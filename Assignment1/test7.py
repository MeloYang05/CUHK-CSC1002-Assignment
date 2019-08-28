Guess_Number='856'
a=0
Number_list=list()
for i in range(100,1000):
    i=str(i)
    Number_list.append(i)
Number_list_0=list()
for h in Number_list:
    set1=set(Guess_Number)
    set2=set(h)
    set3=set1&set2
    list1=list(set3)
    c=len(list1)
    if c==int(a):
        Number_list_0.append(h)
Number_list=Number_list_0
print(Number_list)