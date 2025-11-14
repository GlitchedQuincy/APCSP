#import necessary libraries - PD, PLT, NP
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  
import re

# create our data frame using our csv
data = pd.read_csv('xmas.csv')

# turn data into a dataframe(df)
df = pd.DataFrame(data)

# Count how many times each food was chosen across the separated columns F1..F11.
# Exclude the combined "Foods" column and any blank values ("").
f_cols = [c for c in df.columns if re.match(r'^F\d+$', c)]  # only F1, F2, ... F11

# Stack values from the F columns into one Series, trimming whitespace
stacked = df[f_cols].applymap(lambda x: x.strip() if isinstance(x, str) else x).stack()

# Drop real NaNs, convert to string, strip again and remove unwanted entries
all_choices = stacked.dropna().astype(str).str.strip()

# Remove empty strings, strings that are only quotes (e.g. '""'), and literal 'nan'/'none'
valid_mask = (
    (all_choices != '') &
    (~all_choices.str.fullmatch(r'"*')) &
    (~all_choices.str.lower().isin(['nan', 'none']))
)
all_choices = all_choices[valid_mask]

counts = all_choices.value_counts()

# Plot: include every option (no "Other" grouping) and set the requested title
pie_series = counts.sort_values(ascending=False)

labels = pie_series.index.tolist()
sizes = pie_series.values.tolist()

plt.figure(figsize=(10,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('favorite things to have during christmas')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Optional: bar chart of the top 20 exact counts for more clarity
plt.figure(figsize=(10,6))
counts.head(20).sort_values().plot(kind='barh', color='C0')
plt.title('Food choice counts (top 20) from F1-F11')
plt.xlabel('Count')
plt.tight_layout()
plt.show()

