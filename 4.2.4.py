import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)

# write the code
daily_transactions = df.groupby('Date')['Product'].apply(list)
# Initialize a Counter to store the frequency of each pair
pair_counts = Counter()
# 2. Iterate through each date's transaction
for products in daily_transactions:
# Sort the products to ensure (A, B) is treated the same as (B, A)
	products = sorted(products)
# Generate all possible pairs (combinations of size 2)
# If a date has fewer than 2 products, this produces nothing(correctly)
	pairs = list(combinations(products, 2))
# Update the counter with these pairs
	pair_counts.update(pairs)
# 3. Find the maximum frequency count and print all pairs that matchthis maximum frequency
if pair_counts:
	max_count = max(pair_counts.values())
	for pair, count in pair_counts.items():
		if count == max_count:
			print(f"{pair[0]} and {pair[1]}: {count} times")
else:
	print("No product pairs found.")
