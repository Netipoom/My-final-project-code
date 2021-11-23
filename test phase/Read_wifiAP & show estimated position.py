a='B8:EC:A3:09:E3:53'
b='9C:A5:C0:03:AD:6C'
d='C0:FD:84:DB:48:ED'
cell=[]
ax=input('actual x: ')
ay=input('actual y: ')
import csv
import numpy as np
import time 
import requests
import json
import matplotlib.pyplot as plt
for i in range(15):
    cell=[]
    url = "http://192.168.43.78:5000/"

    response = requests.get(url)

    data = response.text
    

    parsed = json.loads(data)
    c=0
    d1={}
    data=data.split(',')
    for i in data:
        i=i.strip(' \n"')
        i=i.split(': ')
        if len(i)!=1 and (i[1].split('"')[0].strip()== a or i[1].split('"')[0].strip()== b or i[1].split('"')[0].strip()== d):
            cell.append((i[1].split('"')[0].strip()))
            c+=1
        #print(i)
        if i[0].startswith("ESSID") and c==1:
            line2=i[0].split(":")
            cell.append(line2[1].strip('\\').strip('"'))
        if i[0].startswith("Quality") and c==1:
            line5=i[0].split()
            line6=line5[2].split("=")
            cell.append(line6[1])
            c=0
            d1[line2[1].strip('\\').strip('"')]=int(line6[1].split('/')[0])
    print(d1)
    csv.register_dialect('ssv', delimiter=' ', skipinitialspace=True)
    c=0
    data = []
    key=[]
    with open('filtered_train.txt', 'r') as f:
        reader = csv.reader(f, 'ssv')
        for row in reader:
            c+=1
            if c!=1:
                
                floats = [column.strip().split('\t') for column in row]
                floats = list(map(float, floats[0]))
                data.append(floats)
            else:
                key=row[0].split('\t')
                #print(key)
    data=np.array(data)
    data2=abs(data[:,0:3]-np.array([d1[key[0]],d1[key[1].strip('"')],d1[key[2].strip('"')]]))
    #print (data2)
   
    data[:,0:3]=data2[:,0:3]
    #print(data)
    d2={}
    for line in data:
        x=str(line[3])+','+str(line[4])
        if x not in d2.keys():
            d2[x]=[]
            for line1 in line[0:3]:
                #print(line)
                d2[x].append(line1)
        else:
            for line1 in line[0:3]:
                d2[x].append(line1)
    #print(d)
    v=(min(d2, key=d2.get))
    print(v)
    print('\n')
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, 21, 1))
    ax.set_yticks(np.arange(0, 21.,1))
    plt.plot(int(v[0]), int(v[1]),label='estimated point')
    plt.xlabel('x [m/2]')
    plt.ylabel('y [m/2]')
    textfile = open("test.txt", "a")
    textfile.write(key[0]+'\t'+key[1].strip('"')+'\t'+key[2].strip('"')+'\t'+'est x'+'\t'+'est y'+'\t'+'act x'+'\t'+'act y')
    textfile.write('\n')
    textfile.write(str(d1[key[0]])+'\t'+str(d1[key[1].strip('"')])+'\t'+str(d1[key[2].strip('"')])+'\t'+v.split(',')[0]+'\t'+v.split(',')[1]+'\t'+ax+'\t'+ay)
    textfile.write('\n')
    textfile.close()
    time.sleep(5)
















    
        
