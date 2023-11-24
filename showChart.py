import pandas as pd
import numpy as np

dataProp1 = ["chinaHistory.json", "名称", "开始年份", "结束年份"]
dataProp2 = ["monarkies.json", "monarchy", "Born", "Born"]
dataProp3 = ["tangPoets.json", "姓名", "出生年份", "逝世年份"]
dataProp4 = ["songPoets.json", "姓名", "出生年份", "逝世年份"]

inputFile = dataProp4

dataFile = inputFile[0]
dataKey = inputFile[1]
dataStartYear = inputFile[2]
dataEndYear = inputFile[3]

df = pd.read_json(dataFile)
df['delta'] = df[dataEndYear] - df[dataStartYear]
df['color'] = np.where(df['color'].isnull(), "0", "1")
df["color"] = df["color"].astype(str)


# Add filters here.
#df = df[df.Born > 1000]

# Sorting by column
df = df.sort_values(by=[inputFile[2]])


import plotly.express as px
import pandas as pd

sortList = df[dataKey].tolist().copy()
print(sortList)

fig = px.timeline(df, x_start=dataStartYear, x_end=dataEndYear, y="姓名", color = "color", template="plotly_white", opacity = .75, category_orders={"姓名":sortList})

fig.layout.xaxis.type = 'linear'

print(fig.data)

for d in fig.data:
    filt = df['color'] == d.name
    d.x = df[filt]['delta'].tolist()    


f = fig.full_figure_for_development(warn=False)
fig.show()

##df = pd.DataFrame([
##    dict(Task = "Task A", Start = '2013-09-05', End = '2013-10-25', Assigned = "Person A", Difficulty = 70),
##    dict(Task = "Task B", Start = '2013-12-03', End = '2014-02-14', Assigned = "Person A", Difficulty = 20),
##    dict(Task = "Task C", Start = '2013-10-20', End = '2014-03-17', Assigned = "Person B", Difficulty = 30),
##    dict(Task = "Task D", Start = '2014-02-21', End = '2014-07-06', Assigned = "Person A", Difficulty = 50),
##    dict(Task = "Task E", Start = '2014-06-20', End = '2014-09-28', Assigned = "Person B", Difficulty = 80)
##])

###fig = px.timeline(df, x_start = "Born", x_end = "Died", y = "monarchy")
##fig = px.timeline(df, x_start = "Start", x_end = "End", y = "Task")
##
### Tasks from top to bottom
##fig.update_yaxes(autorange = "reversed") 
##fig.show()