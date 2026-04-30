import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

# Data Cleaning
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop('Cabin', axis=1, inplace=True)

# Convert categorical features to numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Write your code here for Box Plot for Fare by Pclass

# Create the boxplot for Fare by Pclass
plt.figure(figsize=(8,6))
data.boxplot(column='Fare', by='Pclass')
# Customize titles and labels
plt.suptitle('')
plt.title("Fare by Pclass")
# Removes the default "Boxplot grouped by Pclass"subtitle
plt.xlabel("Pclass")
plt.ylabel("Fare")
# Display the plot
plt.show()
