# Hello Fresh Technical Assignment
### Engineering Intern - Anique Lodewijkx

Hello! My name is Anique Lodewijkx and this is my submission for the technical assignment for the HelloFresh Engineering Intern position.

The code file I've submitted in this repository ('Hello_Fresh_Anique.py') was run with Python 3.9.12. The packages used are detailed in 'requirements.txt'. The .py file relies on the file ('recipes.txt') also found in this repository.
The resulting csv file ('recipes_anique_lodewijkx.csv') can be found in the recipes-etl directory.

## Hello_Fresh_Anique.py

My code submission is organised with comments above the lines of code pertaining to them. The main two tasks, filtering for recipes using chilis and assigning a difficulty level to these recipes, are titled with a comment in all capital letters. Throughout my code I have multiple print statements; this is because I prefer to visualise the data along the way so that I can see whether anything unexpected is happening.

The code works by first reading the recipes.txt file as a json file and loading it into a Pandas dataframe. This allowed me to have a better overview of the data and to use the very useful Pandas methods for cleaning and organising it. For the first task of filtering the dataframe to include only the recipes which have chilis, I first made a column 'has_chili' which is True or False depending on the occurrence of the string 'chilies' or similar misspellings in the ingredients column. Then, a new dataframe 'chili_recipes' is instantiated which only includes the rows for which 'has_chili' is True. Once this process is done, the 'has_chili' column can be removed because its only purpose was to be used for the conditional check. Also, the index column is removed as it represents the index of the row in the previous dataframe, 'recipes', instead of the current one 'chili_recipes'.

Secondly, in order to assign a difficulty level to the chili recipes, the time format of the cookTime and prepTime columns must be changed so that they can be added together. This is of course not possible with a combination of digits and characters. After removing the character 'PT' from both columns, I use a function to transform the remaining values into timedelta objects. This is more useful than simply summing the number of minutes (M), because it will automatically transform the value into 1 hour if it exceeds 60. For example, we would like prepTime 15M + cookTime 45M to be 1H instead of 60M. Timedelta also allows for an easy summing of the prepTime and cookTime columns in a simple addition. Lastly, I used a lambda function to assign the difficulty label depending on the value of the total time variable using pandas .apply() method. For every total time _x_, if x is greater than 1 hour, the chili_recipes column 'difficulty' takes on the value 'Hard'. If this value is less than an hour but higher than 30 minutes, it will take on 'Medium' label, and otherwise the 'Easy' label.

Finally, I saved the pandas dataframe chili_recipes with added column 'difficulty' to a csv called recipes_anique_lodewijkx.csv'.

I hope this was sufficiently explained and please let me know if I can clarify anything. Thank you for reading!
