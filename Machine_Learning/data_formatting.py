import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

#TRAIN TEST SPLIT

 # create X and y dataframes for training/testing
X = sdf1.loc[:,sdf1.columns != 'result'].values
y = sdf1.loc[:,sdf1.columns == 'result'].values
groups = sdf1['match_id']

from sklearn.model_selection import GroupKFold
# 80/20 split for train/test groups
gkf = GroupKFold(n_splits=5)

for train_index, test_index in gkf.split(X, y,groups):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

# PREPARE TRAINING DATA FOR NEURAL NETWORK
# reshape data to work with previously written parse_game function
xtrain = pd.DataFrame(X_train)
ytrain = pd.DataFrame(y_train)
train_df = pd.merge(xtrain, ytrain, left_index=True, right_index=True)
train_df.rename(columns={'0_y':'result','0_x':'match_id'},inplace=True)
train_df.sort_values(['match_id',1],inplace=True)

# PREPARE TESTING DATA FOR NEURAL NETWORK

def parse_game(grp):
    """Input is a single groupby object
    Output is a list of 3d arrays, each element contains 10 rows (which are equivalent to minutes 
       for this dataset). The function tracks the length of each group and stops at length minus 1. 
       After a group is finished the function performs the same process on the next group.
    """  
    t = 10
    start = 0
   
    length = len(grp)

    while t < length:
        
        # take a 10 row chunk and convert it to array
        
        data = grp.iloc[:,2:-1][start:t].values
   
        df_list.append(data)
        result_list.append(grp.iloc[:,-1:][start:t].values[0])
        
        # stop when t reaches length - 1
        start += 1
        t += 1
    
    return df_list  


xtest = pd.DataFrame(X_test)
ytest = pd.DataFrame(y_test)
test_df = pd.merge(xtest, ytest, left_index=True, right_index=True)   
test_df.rename(columns={'0_y':'result','0_x':'match_id'},inplace=True)

# PARSE GAME DATA TO RESHAPE
df_list = []
result_list = []
gb = train_df.groupby('match_id')
gb.apply(lambda group: parse_game(group));

num_features = 22
time_steps = 10

# reshape y to 1d numpy array
length_r = len(result_list)
y_train = np.array(result_list)
y_train = y_train.ravel()

# reshape x to 3d numpy array
length = len(df_list)
X_train = np.array(df_list)
X_train = X_train.reshape((length, time_steps, num_features))

# PARSE TEST GAME DATA TO RESHAPE

def parse_game_test(grp):
    """Inputs are 1. a groupby group object
    Output is a list of 3d arrays, each element contains 10 rows (which are equivalent to minutes 
       for this dataset). The function tracks the length of each group and stops at length minus 1. 
       After a group is finished the function performs the same process on the next group.
    """  
    t = 10
    start = 0
   
    length = len(grp)

    while t < length:
        
        # take a 10 row chunk and convert it to array
        
        data = grp.iloc[:,2:-1][start:t].values
   
        df_list_test.append(data)
        result_list_test.append(grp.iloc[:,-1:][start:t].values[0])
        
        # stop when t reaches length - 1
        start += 1
        t += 1
    
    return df_list 


df_list_test = []
result_list_test = []
gb = test_df.groupby('match_id')
gb.apply(lambda group: parse_game_test(group));

length_r = len(result_list_test)
y_test = np.array(result_list_test)
y_test = y_test.ravel()

length = len(df_list_test)
X_test = np.array(df_list_test)
X_test = X_test.reshape((length, time_steps, num_features))

print("X_train shape: ", X_train[:-4].shape)
print("y_train shape: ", y_train[:-4].shape)
print("X_test shape: ", X_test[:-31].shape)
print("y_test shape: ", y_test[:-31].shape)