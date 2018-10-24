import pygal
import csv
from datetime import datetime

filename='activity.csv'
count=0
step, date, interval = [], [], []
with open(filename) as fl:
    reader=csv.reader(fl)
    header_row=next(reader)
    for column in reader:
        steps=column[0]
        if steps=='NA':
            try:
                step.append(0)
            except ValueError:
                continue
        else:
           step.append(steps)
    fl.seek(0)
    next(fl)
    for column in reader:
        dates=column[1]
        try:
            if dates in date:
                continue
            else:
                date.append(dates)
        except ValueError:
            continue
    fl.seek(0)
    next(fl)
    for column in reader:

        intervals=column[2]
        try:
            interval.append(intervals)
        except ValueError:
            continue
    fl.seek(0)
    next(fl)
    for column in reader:

        steps=column[0]
        try:
            if steps=='NA':
                count += 1
        except ValueError:
            continue
    fl.seek(0)
    next(fl)
    stepsDay = []
    totalSteps = 0
    current_date = datetime.strptime('2012-10-1', "%Y-%m-%d")
    for column in reader:
        current_dates = datetime.strptime(column[1], "%Y-%m-%d")
        if current_dates == current_date:
            try:
                step = int(column[0])
                totalSteps += step
            except ValueError:
                continue
        else:
            current_date = current_dates
            stepsDay.append(totalSteps)
            totalSteps = 0

hist = pygal.Bar()
hist.add("Steps", stepsDay)
hist.title = "Number of steps per day"
hist.x_labels = date
hist.x_title = 'Date'
hist.y_title = "Steps"
hist.render_to_file("total_steps_day2.svg")

print(stepsDay)
print(date)
print(interval)
print(count)
sort=sorted(stepsDay)
median=len(sort)/2
print(sort[int(median)])
total=sum(stepsDay)
means=total/len(stepsDay)
print(means)
