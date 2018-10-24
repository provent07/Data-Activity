import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='activity.csv'
with open(filename) as fl:
    reader=csv.reader(fl)
    header_row=next(reader)

    steps, date,interval = [], [],[]
    weeks=[]
    weekdays=[]
    weekends=[]

    current_date = datetime.strptime('2012-10-1', "%Y-%m-%d")
    for column in reader:
        dates = column[1]
        date.append(dates)

        current_dates = datetime.strptime(column[1], "%Y-%m-%d")
        if current_dates == current_date:
            try:
                inter = int(column[2])
                interval.append(inter)
            except ValueError:
                continue
        else:
            break

    date = list(set(date))

    print("first read finished")

    stepsOccur = []
    stepsIntervalweekdays = []
    stepsIntervalweekends =[]
    totalStepsweekday = 0
    totalStepsweekend =0
    count=0
    print("after count")

    for x in interval:
        fl.seek(0)
        next(fl)
        for column in reader:
            inter = int(column[2])
            try:
                if x==inter:
                    for i in date:
                        current_dates = datetime.strptime(column[1], "%Y-%m-%d")
                        if current_dates == i:
                            if count%7<5:
                                totalStepsweekday+= (int(column[0]))
                            elif count%7>4:
                                totalStepsweekend+= (int(column[0]))
                        else:
                            if count%7<5:
                                totalStepsweekday+= (int(column[0]))
                            elif count%7>4:
                                totalStepsweekend+= (int(column[0]))
                            count+=1
                else:
                    continue
            except ValueError:
                continue
        stepsIntervalweekdays.append(totalStepsweekday)
        stepsIntervalweekends.append(totalStepsweekend)
        totalStepsweekday=0
        totalStepsweekend = 0
    print(count)

    print("read 2")
    count = len(stepsIntervalweekdays)
    print (count)
    counts = len(stepsIntervalweekends)


    for x in stepsIntervalweekdays:
        x = x /count
        weekdays.append(x)
    for x in stepsIntervalweekends:
        x = x / counts
        weekends.append(x)

print (weekdays)
print(stepsIntervalweekends)
fig=plt.figure(dpi=128,figsize=(70,6))
plt.plot(interval,weekdays,c='red',alpha=0.5)
plt.plot(interval,weekends,c='blue',alpha=0.5)
plt.legend(["Weekdays","Weekends"])
plt.xlabel('Intervals',fontsize=16)
plt.ylabel('Average Steps',fontsize=16)
plt.axis([0,2500,0,70])
plt.show()