# %%
# Import necessary libraries
import pandas as pd
import json
import datetime

# Read the JSON file
file_path = 'recipes.txt'
with open(file_path, 'r') as file:
    data = [json.loads(line) for line in file]

# Load JSON into pandas dataframe
recipes = pd.json_normalize(data)

# Separate ingredients by '. ' instead of '\n' for readability
recipes.ingredients = recipes.ingredients.str.replace('\n','. ')

# Display dataframe
recipes.head()

# %%
# FILTER RECIPES TO ONLY CHILI RECIPES

# Create pandas series with all ingredients in lowercase letters
ingredients_lowercase = recipes.ingredients.str.lower()

# Find all ingredients with 'chilies' (including spelling errors) in ingredients
has_chilies = ingredients_lowercase.str.contains('chilies|chilis|chillies|chile|chilles|chili|chilli ')

# Make new df column 'has_chili' with True or False
recipes['has_chili'] = has_chilies

# Create new dataframe including only rows where 'has_chili' is True
chili_recipes = recipes[recipes['has_chili']].reset_index() # Reset index to start from 0

# Remove old index column
chili_recipes.drop('index', axis=1, inplace=True)

# Display dataframe with new column
chili_recipes.head()

# %%
# ADD RECIPE DIFFICULTY

# Remove 'PT' from cookTime and prepTime columns
cookTime_noPT = chili_recipes.cookTime.str.replace('PT','')
prepTime_noPT = chili_recipes.prepTime.str.replace('PT','')

# Display new columns
print(prepTime_noPT, cookTime_noPT)

# %%
# Function to convert str into timedelta format
def convert_to_timedelta(time):
    hours, minutes = 0, 0
    
    # Extract hours and minutes from the string
    if 'H' in time:
        hours = int(time.split('H')[0])
    if 'M' in time:
        minutes = int(time.split('M')[0].split('H')[-1])
    
    # Create a timedelta object
    return pd.Timedelta(hours=hours, minutes=minutes)

# Apply function to cleaned cook and prep time columns
new_cookTime = cookTime_noPT.apply(convert_to_timedelta)
new_prepTime = prepTime_noPT.apply(convert_to_timedelta)

# Sum cook and prep times per row
total_time = new_cookTime + new_prepTime


# Create new column 'Difficulty' with
    # 'Hard' for total time greater than 1 hour
    # 'Medium' for total time less than 1 hour but greater 30 minutes
    # 'Easy' for total time 30 minutes or less
chili_recipes['difficulty'] = total_time.apply(lambda x: 'Hard' if x > pd.Timedelta(hours=1) else 'Medium' if x > pd.Timedelta(minutes=30) else 'Easy')

# %%
# Display dataframe to ensure correct columns added, 'has_chili' and 'difficulty'
chili_recipes.head()

# Save dataframe as csv file
chili_recipes.to_csv('recipes_anique_lodewijkx.csv')


