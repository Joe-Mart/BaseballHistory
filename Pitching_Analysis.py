# Pitching project for Code Louisville Python Class 1.

import pandas as pd
import numpy as np
from sqlalchemy import false
import math

# from matplotlib import pyplot as plt


# Pitching.csv came from the Kaggle database located at
# https://www.kaggle.com/open-source-sports/baseball-databank

# 1. Use pd.read_csv('data\Pitching.csv') to create a DataFrame called pitching.
# 2. Use .head() to display the first 5 rows of the dataset.

pitching = pd.read_csv('data\Pitching.csv')
pitching.head()

# Since the data contains entries from 1871 to 2015, need to narrow the size of the
# database.  In 1950, Major League Baseball set the pitching mound at 15 inches high.
# Because of complaints from batters in "The year of the pitcher (1968)", MLB lowered
# the mound height to ten inches. So, data will cover from 1965 to 1972, four years before
# and after the mound height was lowered.

# Update the dataset to include only rows from 1965 to 1972, had a minumu of 20 starts
# each season, and have no relief appearances,  In addition, keep only the first 20 columns.

pitching['yearID'] = pitching['yearID'].astype(float)

pitching = pitching[(pitching['yearID'] >= 1965) & (pitching['yearID'] <= 1972) & (pitching['GS'] >= 20) & (pitching['G'] == pitching['GS'])].iloc[:, :20]
pitching = pitching.drop(['stint', 'W', 'L', 'CG', 'SHO', 'SV'], axis=1)
pitching.head()

# The pitching sample script on Kaggle has calculation for other pitching metrics.  I decided to include some of those metrics for 
# possible future use.
# the analysis here is to analyze the Earned Run Average (ERA) from 1965 to 1972 to see if lowering the mount height in 1969
#  did have an impact on pitching ERA.

# The first set up is to create a column that computes the number of innings pitched.  The data has a field called IPouts which
# shows the total outs pitched by pitcher.  So, simply, take this number and divide by 3 to get the innings.  Round the decimal to two digits.
# Once the column is created, there is no need for the IPouts column, so that will be deleted.

pitching['IP'] = ((pitching['IPouts'])/3).round(2)
del pitching['IPouts']
pitching.head()

# With the number of innings pitched, we can now calculate the strikeouts per nine innings and the walks per nine innings.
# These two columns will be showing to see if lowering impacted the strikeouts per nine and walks per nine innings.

# For the strikeouts per nine, perform the calculation of selecting the `SO` column, multiplying it by 9, and dividing by the `IP` column.
# Use .round(2) to round the results to 2 decimal places.

pitching['SO9'] = (pitching['SO'] * 9 / pitching['IP']).round(2)

# For the walks per nine inning, perform the calculation of selecting the `BB` column,  multiplying it by 9, and then dividing by the `IP` column.
# Use .round(2) to round the results to 2 decimal places.
# Use .head() to display the first 5 rows of the updated dataset.

pitching['BB9'] = (pitching['BB'] * 9 / pitching['IP']).round(2)
pitching.head()

# Create the Strikeout to Walk ratio by performing the calculation of selecting the `SO` column and dividing by the `BB` column.
# Use .round(2) to round the results to 2 decimal places.
# Use .head() to display the first 5 rows of the updated dataset.

pitching['SOtoBB'] = (pitching['SO'] / pitching['BB']).round(2)
pitching.head()

# Eventually, I plan to show the information in a graph.  For this class, I plan to just show the dataframe.
# Grouping the yearID, show the average ERA, SO9 and BB9 and SOtoBB ratio.

# Created an empty dataframe called pitching_averages to create columns

column_names = ["avg_era", "avg_SO9", "avg_BB9", "avg_SOtoBB"]

pitching_averages = pd.DataFrame(columns = column_names)

pitching_averages = pitching_averages.append(pitching.groupby(['yearID'], as_index = False).agg(avg_era = ('ERA', 'mean'), avg_SO9 = ('SO9', 'mean'), \

avg_BB9 = ('BB9', 'mean'), avg_SOtoBB = ('SOtoBB', 'mean')))

# Round the averages to two decimal places.

pitching_averages = pitching_averages.round({"avg_era":2, "avg_SO9":2, "avg_BB9":2, "avg_SOtoBB":2, "yearID":0})

# pitching_averages['yearID']=int(float(pitching_averages['yearID']))


# Reorder the columns in the dataframe to have the YearID column first.

pitching_averages = pitching_averages[['yearID', 'avg_era', 'avg_SO9', 'avg_BB9', 'avg_SOtoBB']]

pitching_averages['yearID'] = pitching_averages['yearID'].astype(int)

print(pitching_averages)