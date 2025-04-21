import pandas as pd
df = pd.read_csv('moviesdataset.csv')

cleaned = df.drop_duplicates()

cleaned.columns = cleaned.columns.str.strip().str.lower().str.replace(' ','_')

cleaned['date_added'] = pd.to_datetime(cleaned['date_added'], errors='coerce')

cleaned = cleaned.dropna(subset=['title', 'release_year','genres'])

cleaned['description'] = cleaned['description'].fillna('No description')
cleaned['cast'] = cleaned['cast'].fillna('Cast not listed')
cleaned['country'] = cleaned['country'].fillna('Unknown')
cleaned['director'] = cleaned['director'].fillna('unknown')

cleaned['language'] = cleaned['language'].str.strip().str.lower()
cleaned['type'] = cleaned['type'].str.strip().str.title()

cleaned['release_year'] = cleaned['release_year'].astype(int)
cleaned['rating'] = cleaned['rating'].astype(float)
cleaned['vote_count'] = cleaned['vote_count'].astype(int)
cleaned['vote_average'] = cleaned['vote_average'].astype(float)

cleaned.to_csv('cleaned_moviesdataset.csv', index=False)

print("Modified cleaning complete:")
print(f"Original rows: {len(df)}")
print(f"Rows after cleaning: {len(cleaned)}")
print(f"Duplicates removed: {len(df) - len(df.drop_duplicates())}")
print(f"Rows dropped due to missing critical data: {len(df.drop_duplicates()) - len(cleaned)}")
