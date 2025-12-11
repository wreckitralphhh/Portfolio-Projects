# There are 50,000 iterations in the raw file and that way too much to look at 
# Let's assume we set divide the 50K into chunks and take a look at each "checkpoint"
# Let's say every "checkpoint" == 10K iterations and we will look at the 10Kth plot

import pandas as pd 
import matplotlib.pyplot as plt

#loads in CSV, make sure you use a raw string or \\ on windows 
#importing Path and using it doesn't work for some reason
df = pd.read_csv(r"C:\Users\Ralph\Desktop\test_engineer_data.csv")

#prints top of dataset, just making sure it arrive safely
print(df.head())

# this will let us group the dataset, by iteration 
groups = [g for _, g in df.groupby(df.index // 20)]
group_indices = [0, 10000, 20000, 30000, 40000, 49999]  # the 5 groups



def plot_all_groups():
    fig, axes = plt.subplots(len(group_indices), 1, figsize=(10, 12), sharex=False)
    for i, idx in enumerate(group_indices):
        g = groups[idx].copy()
        
        # Convert timestamp to datetime if needed
        g['Timestamp (s)'] = pd.to_datetime(g['Timestamp (s)'])

        # Relative time
        g['t_rel'] = (g['Timestamp (s)'] - g['Timestamp (s)'].iloc[0]).dt.total_seconds()
        
        axes[i].scatter(g['t_rel'], g['Encoder (deg)'], c='blue')
        axes[i].plot(g['t_rel'], g['Encoder (deg)'], c='red', linewidth=1, label='Line')
        axes[i].set_title(f'Group {idx}')
        axes[i].set_ylabel('Encoder (deg)')
        axes[i].grid(True)

    axes[-1].set_xlabel('Relative Time (sec)')  # only the bottom plot gets an x-label

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_all_groups()