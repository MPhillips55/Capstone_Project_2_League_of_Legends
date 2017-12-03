import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('df.csv',index_col=0)

# fit StandardScaler
data = df.iloc[:,2:-1]
scaler = StandardScaler()
scaler.fit(data)

# DATA FORMATTING
# want to keep group/result columns and add them back after scaling
cols = list(df.columns.values)
hold_out_cols = ['match_id', 'time', 'result']
ho_df = df[hold_out_cols].copy()

cols_scale = ['gold', 'top_gold', 'jgl_gold', 'mid_gold', 'adc_gold', 'sup_gold', 'kill_total',
 'assist_total', 'opp_kill_total', 'opp_assist_total', 'r_inhib_count', 'r_baron_count', 'r_tower_count',
 'r_herald_count', 'r_drag_count', 'b_inhib_count', 'b_baron_count', 'b_tower_count', 'b_herald_count',
 'b_dragon_count', 'kda', 'opp_kda']

# scale data
data = scaler.transform(data)

sdf = pd.DataFrame(data)
sdf.columns = cols_scale

# Merge holdout columns with scaled data
sdf = pd.merge(sdf, ho_df, left_index=True, right_index=True)

fcols = [ 'match_id', 'time','gold', 'top_gold', 'jgl_gold', 'mid_gold', 'adc_gold', 'sup_gold', 'kill_total',
 'assist_total', 'opp_kill_total', 'opp_assist_total', 'r_inhib_count', 'r_baron_count', 'r_tower_count',
 'r_herald_count', 'r_drag_count', 'b_inhib_count', 'b_baron_count', 'b_tower_count', 'b_herald_count',
 'b_dragon_count', 'kda', 'opp_kda', 'result']

sdf1 = sdf[fcols]

g2r = sdf1.loc[(sdf1['match_id'] == '2a1d6285ce9dd71f_r'),:]
g2b = sdf1.loc[(sdf1['match_id'] == '2a1d6285ce9dd71f_b'),:]

def parse_single_game(df):
    """Input is a single groupby object
    Output is a list of 3d arrays, each element contains 10 rows (which are equivalent to minutes 
       for this dataset). The function tracks the length of each group and stops at length minus 1. 
       After a group is finished the function performs the same process on the next group.
    """  
    t = 10
    start = 0
   
    length = len(df)

    while t < length:
        # take a 10 row chunk and convert it to array
        data = df.iloc[:,2:-1][start:t].values
   
        df_list.append(data)
        result_list.append(df.iloc[:,-1:][start:t].values[0])
        
        # stop when t reaches length - 1
        start += 1
        t += 1
    
    #return df_list    

df_list = []
result_list = []
parse_single_game(g2b)

num_features = 22
time_steps = 10

# reshape y to 1d numpy array
length_r = len(result_list)
yg2b = np.array(result_list)
yg2b = yg2b.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg2b = np.array(df_list)
xg2b = xg2b.reshape((length, time_steps, num_features))

df_list = []
result_list = []
parse_single_game(g2r)

# reshape y to 1d numpy array
length_r = len(result_list)
yg2r = np.array(result_list)
yg2r = yg2r.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg2r = np.array(df_list)
xg2r = xg2r.reshape((length, time_steps, num_features));