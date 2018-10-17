import csv
from datetime import  datetime
import pygal

filename='activity.csv'
with open(filename) as fl:
    reader=csv.reader(fl)
    header_row=next(reader)


    steps, date = [], []
    stepsDay=[]
    totalSteps = 0
    current_date = datetime.strptime('2012-10-1', "%Y-%m-%d")
    for column in reader:
        current_dates = datetime.strptime(column[1], "%Y-%m-%d")
        if current_dates==current_date:
            try:
                step = int(column[0])
                totalSteps += step
            except ValueError:
                continue
        else:
            date.append(current_date)
            current_date=current_dates
            stepsDay.append(totalSteps)
            totalSteps = 0

date.append(datetime.strptime('2012-11-30', "%Y-%m-%d"))
stepsDay.append(0)
hist=pygal.Bar()
hist.add("Steps",stepsDay)
hist.title="Number of steps per day"
hist.x_labels=date
hist.x_title='Date'
hist.y_title="Steps"
hist.render_to_file("total_steps_day.svg")
sort=sorted(stepsDay)
print(sort)
median=len(sort)/2
print(sort[int(median)])
total=sum(stepsDay)
means=total/len(date)
print(date)
print(len(date))
print(means)
