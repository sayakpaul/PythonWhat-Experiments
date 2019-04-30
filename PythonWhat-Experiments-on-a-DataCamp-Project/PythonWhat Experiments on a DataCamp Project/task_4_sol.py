import pandas as pd
import numpy as np

# Load dataset
cc_apps = pd.read_csv("datasets/cc_approvals.data", header=None)

# Replace the '?'s with NaN
cc_apps = cc_apps.replace('?', np.nan)

# Impute the missing values with mean imputation
cc_apps.fillna(cc_apps.mean(), inplace=True)