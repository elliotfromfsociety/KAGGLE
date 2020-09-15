# Regular Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

import warnings
warnings.filterwarnings("ignore")

space_missions = pd.read_csv("../input/all-space-missions-from-1957/Space_Corrected.csv")

#data preprocessing 
space_missions['DateTime'] = pd.to_datetime(space_missions['Datum'])

# Extract the launch year
space_missions['Year'] = space_missions['DateTime'].apply(lambda datetime: datetime.year)

# Extract the country of launch
space_missions["Country"] = space_missions["Location"].apply(lambda location: location.split(", ")[-1])

space_missions.head(10)

plt.figure(figsize=(8,18))
ax = sns.countplot(y="Company Name", data=space_missions, order=space_missions["Company Name"].value_counts().index)
ax.set_xscale("log")
ax.axes.set_title("Company vs. # Launches (Log Scale)",fontsize=18)
ax.set_xlabel("Number of Launches (Log Scale)",fontsize=16)
ax.set_ylabel("Company Name",fontsize=16)
ax.tick_params(labelsize=12)
plt.tight_layout()
plt.show()
