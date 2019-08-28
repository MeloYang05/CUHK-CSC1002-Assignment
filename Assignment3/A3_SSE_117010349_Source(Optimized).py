import math
from functools import reduce, partial
from collections import Counter
from time import strftime,gmtime,localtime
import random

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def sum_of_squares(v):
    return sum(v_i * v_i for v_i in v)

def distance(v, w):
    s = vector_subtract(v,w)
    return math.sqrt(sum_of_squares(s))

def new_dict(a):
    a_dict=dict()
    with open (a) as file_object:
        small_count=0
        huge_count=0
        for line in file_object:
            small_count=small_count+1
            if small_count==1:
                vector_list=list()
            if len(line)>7:
                line_list=list()
                for i in line:
                    if i.isdigit():
                        line_list.append(int(i))
                vector_list.append(tuple(line_list))
            if len(line)<7:
                small_count=0
                huge_count=huge_count+1
                for i in line:
                    if i.isdigit():
                        a_dict[i+'('+str(huge_count)+')']=vector_list
    return a_dict

def predict(m,k):
    distance_dict=dict()
    sample_list=[[],[],[],[],[],[],[],[],[],[]]
    sample_dict=dict()
    for key,value in training_dict.items():
        for i in range(10):
            if int(key[0])==i:
                sample_list[i].append(value)
    count=0
    for i in sample_list:
        sample_list[count]=random.sample(sample_list[count],15)
        count+=1
    count=0
    for i in range(10):
        for j in range(15):
            count+=1
            sample_dict[str(i)+'('+str(count)+')']=sample_list[i][j]
    for number_training,vector_training in sample_dict.items():
        difference=0
        for i in range(0,len(vector_training)):
            if i<0.5*len(vector_training):
                difference+=distance(m[i],vector_training[i])*1.2
            else:
                difference+=distance(m[i],vector_training[i])*0.8   
        distance_dict[number_training]=difference
    distance_list=list()
    for key,value in distance_dict.items():
        distance_list.append((value,key))
        distance_list.sort()
    alternative_list=list()
    for i in range(k):
        alternative_list.append(distance_list[i][1][0])
    alternative_list_counts=Counter(alternative_list)
    result=alternative_list_counts.most_common(1)[0][0]
    return result

starttime=strftime("%Y-%m-%d %H:%M:%S", localtime())

training='digit-training.txt'
testing='digit-testing.txt'
predicting='digit-predict.txt'
training_dict=new_dict(training)
testing_dict=new_dict(testing)
predict_dict=dict()

training_count_list=[0,0,0,0,0,0,0,0,0,0]
testing_count_list=[0,0,0,0,0,0,0,0,0,0]
correct_count_list=[0,0,0,0,0,0,0,0,0,0]
mistake_count_list=[0,0,0,0,0,0,0,0,0,0]
accuracy_list=[0,0,0,0,0,0,0,0,0,0]
number_list=[0,1,2,3,4,5,6,7,8,9]

for key in training_dict:
    for i in number_list:
        if int(key[0])==i:
            training_count_list[i]+=1
for key in testing_dict:
    for i in number_list:
        if int(key[0])==i:
            testing_count_list[i]+=1

for number_testing,vector_testing in testing_dict.items():
    predict_dict[number_testing]=predict(vector_testing,5)

for key,value in predict_dict.items():
    if not key[0]==value:
        mistake_count_list[int(key[0])]+=1

for key,value in predict_dict.items():
    if key[0]==value:
        correct_count_list[int(key[0])]+=1

for i in range(10):
    accuracy_list[i]=correct_count_list[i]/testing_count_list[i]

endtime=strftime("%Y-%m-%d %H:%M:%S", localtime())
        
print('Begin of Training @'+starttime+'\n')
print('----------------------------------------\n')
print('             Training Info              '+'\n')
print('----------------------------------------\n')
for i in range(10):
    print('                '+str(i)+' = '+str(training_count_list[i])+'\n')
print('----------------------------------------\n')        
print('  Total Samples = '+str(sum(training_count_list))+'\n')
print('----------------------------------------\n')
print('             Testing Info               '+'\n')  
print('----------------------------------------\n')
for i in range(10):
    print('            '+str(i)+' = '+str(correct_count_list[i])+',  '+str(mistake_count_list[i])+',  '+str(int(accuracy_list[i]*100))+'%'+'\n')
print('----------------------------------------\n')
print('   Accuracy = '+str(round(sum(correct_count_list)/sum(testing_count_list),2)*100)+'%'+'\n')
print('   Correct/Total = '+str(sum(correct_count_list))+'/'+str(sum(testing_count_list))+'\n')
print('----------------------------------------\n')
print('End of Training @'+endtime+'\n')

for vector_predicting in new_dict(predicting).values():
    print(predict(vector_predicting,5))