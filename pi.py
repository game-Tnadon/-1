import matplotlib.pyplot as plt
import pandas as pd

movies_df = pd.read_csv('imdb2.csv',index_col="Title")
#movies_df = pd.read_csv('D:\New',index_col="Title")#ที่อาจารส่งมา

martin_df = (movies_df['director']) == 'Martin Scorsese' 
print(martin_df.shape)

subset = martin_df[['director', 'revenue_millions']]
print(movies_df[movies_df['director'] == 'Martin Scorsese' ])

def rating_function(x): 
    if x == 79: 
        return "Silence" 
    elif x == 75: 
        return "The Wolf of Wall Street"
    elif x == 85: 
        return "The Departed t"
    elif x == 63: 
        return "Shutter Island "
    elif x == 83: 
        return "Hugo "

movies_df["Martin Scorsese"] = movies_df["score"].apply(rating_function) 
movies_df['Martin Scorsese'].value_counts().plot(kind='bar', title='Scorsese Movies Revenue')


plt.show()