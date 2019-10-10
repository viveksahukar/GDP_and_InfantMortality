# Import libraries
import os
import numpy as np
import pandas as pd

# Read dataset
wdi = pd.read_csv('wdi_data.csv')

# Inspect the dataset
wdi.head()