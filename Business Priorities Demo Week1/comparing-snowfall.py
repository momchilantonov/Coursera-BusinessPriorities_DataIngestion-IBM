#!/usr/bin/env python

import pandas as pd

## read in the data
df = pd.read_csv("./snowfall.csv")

## subset the data to only the states of interest
df1 = df[df['state'].isin(['CO','UT','VT'])]

## create a pivot that looks at the specific data we are interested in
df1_pivot = pd.pivot_table(df1, values='snowfall', index='state', aggfunc=['count', 'mean', 'max'])

print(df1_pivot)
