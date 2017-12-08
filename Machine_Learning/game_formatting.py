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

g1r = sdf1.loc[(sdf1['match_id'] == 'e5af5592e36bdb01_r'),:]
g1b = sdf1.loc[(sdf1['match_id'] == 'e5af5592e36bdb01_b'),:]

g2r = sdf1.loc[(sdf1['match_id'] == '473fc1deff74591b_r'),:]
g2b = sdf1.loc[(sdf1['match_id'] == '473fc1deff74591b_b'),:]

g3r = sdf1.loc[(sdf1['match_id'] == '6ca759012b24b8b1_r'),:]
g3b = sdf1.loc[(sdf1['match_id'] == '6ca759012b24b8b1_b'),:]

g4r = sdf1.loc[(sdf1['match_id'] == '2a1d6285ce9dd71f_r'),:]
g4b = sdf1.loc[(sdf1['match_id'] == '2a1d6285ce9dd71f_b'),:]
                                     
g5r = sdf1.loc[(sdf1['match_id'] == 'ac33fc72f78724a8_r'),:]
g5b = sdf1.loc[(sdf1['match_id'] == 'ac33fc72f78724a8_b'),:]

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

# GAME 1 FORMATTING

df_list = []
result_list = []
parse_single_game(g1b)

num_features = 22
time_steps = 10

# reshape y to 1d numpy array
length_r = len(result_list)
yg1b = np.array(result_list)
yg1b = yg1b.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg1b = np.array(df_list)
xg1b = xg1b.reshape((length, time_steps, num_features))

df_list = []
result_list = []

parse_single_game(g1r)

# reshape y to 1d numpy array
length_r = len(result_list)
yg1r = np.array(result_list)
yg1r = yg1r.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg1r = np.array(df_list)
xg1r = xg1r.reshape((length, time_steps, num_features));

# GAME 2 FORMATTING

df_list = []
result_list = []
parse_single_game(g2b)

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

# GAME 3 FORMATTING

df_list = []
result_list = []
parse_single_game(g3b)

# reshape y to 1d numpy array
length_r = len(result_list)
yg3b = np.array(result_list)
yg3b = yg3b.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg3b = np.array(df_list)
xg3b = xg3b.reshape((length, time_steps, num_features))

df_list = []
result_list = []

parse_single_game(g3r)

# reshape y to 1d numpy array
length_r = len(result_list)
yg3r = np.array(result_list)
yg3r = yg3r.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg3r = np.array(df_list)
xg3r = xg3r.reshape((length, time_steps, num_features));

# GAME 4 FORMATTING

df_list = []
result_list = []
parse_single_game(g4b)

# reshape y to 1d numpy array
length_r = len(result_list)
yg4b = np.array(result_list)
yg4b = yg4b.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg4b = np.array(df_list)
xg4b = xg4b.reshape((length, time_steps, num_features))

df_list = []
result_list = []

parse_single_game(g4r)

# reshape y to 1d numpy array
length_r = len(result_list)
yg4r = np.array(result_list)
yg4r = yg4r.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg4r = np.array(df_list)
xg4r = xg4r.reshape((length, time_steps, num_features));

# GAME 5 FORMATTING

df_list = []
result_list = []
parse_single_game(g5b)

# reshape y to 1d numpy array
length_r = len(result_list)
yg5b = np.array(result_list)
yg5b = yg5b.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg5b = np.array(df_list)
xg5b = xg5b.reshape((length, time_steps, num_features))

df_list = []
result_list = []

parse_single_game(g5r)

# reshape y to 1d numpy array
length_r = len(result_list)
yg5r = np.array(result_list)
yg5r = yg5r.ravel()

# reshape x to 3d numpy array
length = len(df_list)
xg5r = np.array(df_list)
xg5r = xg5r.reshape((length, time_steps, num_features));

