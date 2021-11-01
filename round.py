import pandas as pa
import csv 
import plotly.figure_factory as pf

df=pa.read_csv('classData.csv') 
print(df)

fig=pf.create_distplot([df['Weight(Pounds)'].tolist()],["weight"],show_hist=False)
fig.show()


