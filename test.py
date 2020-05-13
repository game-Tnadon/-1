#Lec9_c6_exercise # bar
import matplotlib.pyplot as plt
import pandas as pd

movies_df = pd.read_csv('imdb2.csv',index_col="Title")

#step1 select rows where director == 'Martin Scorsese'
martin_df =(movies_df[movies_df['director'] == 'Martin Scorsese']) 
print(martin_df.shape) #expect (5,11)

#step2 slice 'director','revenue_millions' columns
subset = martin_df[['director', 'revenue_millions']]
print(subset.head())

#step3 plot bar chart
subset.plot(kind='bar', title='Scorsese Movies Revenue')
plt.show()