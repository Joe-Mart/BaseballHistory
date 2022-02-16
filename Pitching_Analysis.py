# Pitching project for Code Louisville Python Class 1.

import pandas as pd
import numpy as np
import matplotlib as plt


# Pitching.csv came from the Kaggle database located at
# https://www.kaggle.com/open-source-sports/baseball-databank

# 1. Use pd.read_csv('/Pitching.csv') to create a DataFrame called pitching.
# 2. Use .head() to display the first 5 rows of the dataset.

pitching = pd.read_csv('Pitching.csv')
pitching.head()

# Since the data contains entries from 1871 to 2015, need to narrow the size of the
# database.  In 1950, Major League Baseball set the pitching mound at 15 inches high.
# Because of complaints from batters in "The year of the pitcher (1968)", MLB lowered
# the mound height to ten inches. So, data will cover from 1950 to 2015.

# Update the dataset to include only rows from 1950 to 2015, had a minumu of 20 starts
# each season, and have no relief appearances,  In addition, keep only the first 20 columns.

pitching = pitching[(pitching['yearID'] >= 1950) & (pitching['GS'] >= 20) & (pitching['G'] == pitching['GS'])].iloc[:, :20]
pitching = pitching.drop(['stint', 'W', 'L', 'CG', 'SHO', 'SV'], axis=1)
pitching.head()

# The pitching sample script on Kaggle has calculation for other pitching metrics.  All I want to show is the averages of
# the Earned Run Average (ERA) from 1950 to 2015 to see if lowering the mount height in 1969 did have an impact on pitching ERA.

# Create a line chart showing the averages per year

plt =  pitching.groupby('yearID').ERA.mean().plot.line()

