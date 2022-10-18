import pandas as pd
import time

shift_start = []
shift_end = []
shift_temp = []
shift_human = []
shift_temp_temp = []
people = []
date = []
# Creating an empty Dataframe with column names only
user_name = ['User_ID', 'UserName', 'Action',"a","b","c","d","e","f","g","h","i"]
shift = pd.DataFrame(columns=user_name ,index= date)
print("Empty Dataframe ", shift, sep='\n')

for n in range(len(shift_start)):
    for m in range(3):
        if shift_start[m][n] != 0:
            shift.iloc[n ,people] = (shift_start[m][n].strftime("%H:%M") + "~" + shift_end[m][n].strftime("%H:%M"))