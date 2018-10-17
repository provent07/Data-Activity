import csv
from matplotlib import pyplot as plt
from datetime import  datetime

filename='activity.csv'
with open(filename) as fl:
    reader=csv.reader(fl)
    header_row=next(reader)

    steps, date,interval = [], [],[]
    stepsOccur=[]
    stepsInterval = []
    totalSteps = 0
    current_date = datetime.strptime('2012-10-1', "%Y-%m-%d")
    for column in reader:
        current_dates = datetime.strptime(column[1], "%Y-%m-%d")
        if current_dates == current_date:
            try:
                inter = int(column[2])
                interval.append(inter)
            except ValueError:
                continue
        else:
            break
    for x in interval:
        fl.seek(0)
        next(fl)
        for column in reader:
            inter = int(column[2])
            try:
                if x==inter:
                    totalSteps+= (int(column[0]))
                else:
                    continue
            except ValueError:
                continue
        stepsInterval.append(totalSteps)
        totalSteps=0

    n = 0
    for x in stepsInterval:
        x=x/53
        stepsInterval[n] = x
        n+= 1

print(stepsInterval)
print(len(stepsInterval))
print(interval)
print(len(interval))
print(max(stepsInterval))
stepsInterval.index(max(stepsInterval))
print(interval[stepsInterval.index(max(stepsInterval))])

fig=plt.figure(dpi=128,figsize=(70,6))
plt.plot(interval,stepsInterval,c='red',alpha=0.5)
plt.xlabel('Intervals',fontsize=16)
plt.ylabel('Average Steps',fontsize=16)
plt.show()


