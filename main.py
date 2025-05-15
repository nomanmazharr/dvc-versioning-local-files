import pandas as pd
import os

data = {
    'Name' : ['Ali', 'Ahmad', 'Bilal'],
    'Roll_No': [10, 12, 14],
    'email': ['ali@gmail.com', 'ahmad@gmail.com', 'bilal@gmail.com'],
    'DPT': ['CS', 'SE', 'IT'],
    'Timing': ['Morning', 'Evening', 'Weekend']
}

df = pd.DataFrame(data=data)
data_dir = 'data/'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'dataset.csv')
df.to_csv(file_path)
print('file is saved to the directory')