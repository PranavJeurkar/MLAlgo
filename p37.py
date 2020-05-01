import math
import easygui
file = easygui.fileopenbox();
f = open('data2.csv','r')
train = []
while True :
    x = f.readline()
    if x == '':
        break;
    x = x.split(',')
    try :
        home_age = float(x[0])
        dis_metro = float(x[1])
        dis_city = float(x[2])
        latitude = float(x[3])
        longitude = float(x[4])
        price = (x[5])
    except :
        print('Invalid input')
        
    else :
        train.append([home_age,dis_metro,dis_city,latitude,longitude,price])

home_age = int(input('Enter age of house:'))
dis_metro = float(input('Enter distance from metro:'))
dis_city = float(input('Enter disatnce from city center'))
latitude = float(input('Enter latitude'))
longitude = float(input('Enter longitude'))

test = [home_age,dis_metro,dis_city,latitude,longitude,price]

for i in range(0,len(train)):
    a = test[0]
    b = test[1]
    c = test[2]
    d = test[3]
    e = test[4]
    
    a1 = train[i][0]
    b1 = train[i][1]
    c1 = train[i][2]
    d1 = train[i][3]
    e1 = train[i][4]
    
    d = math.sqrt(math.pow(a-a1,2)+math.pow(b-b1,2)+math.pow(c-c1,2)+math.pow(d-d1,2)+math.pow(e-e1,2))
    if i == 0 :
        min_d = d   #min distance
        min_i = i   #min index
    else:
        if d < min_d :
            min_d = d
            min_i = i
price = train[min_i][2]
print('price of house is %s'%(price))