import pandas as pd
import matplotlib.pyplot as plt

form_df = pd.read_csv('./form.csv')

# Clean birth_month
form_df['birth_month'] = form_df['birth_month'].str.strip().str.capitalize()

# Clean state names
state_map = {
    'Kano': 'KN', 'Kaduna': 'KD', 'Abuja': 'AB',
    'Lagos': 'LA', 'Jigawa': 'JG'
}
form_df['state'] = form_df['state'].replace(state_map)
form_df['state'] = form_df['state'].str.upper()

# Clean pet
form_df['pet'] = form_df['pet'].str.capitalize()

# Drop or fill missing state
form_df = form_df.dropna(subset=['state'])  # or .fillna('Unknown')

# Plot again
form_df['state'].value_counts().plot(kind='bar', title="States")
plt.show()

form_df['birth_month'].value_counts().plot(kind='bar', title="Birth Month")
plt.show()
