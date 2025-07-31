import sqlite3
import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('products.csv')

# Step 2: Connect to SQLite database (or create one)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Step 3: Create the 'products' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        stock INTEGER,
        brand TEXT
    )
''')

# Step 4: Insert data from DataFrame into the table
df.to_sql('products', conn, if_exists='replace', index=False)

# Step 5: Verify insertion
cursor.execute('SELECT * FROM products LIMIT 5')
for row in cursor.fetchall():
    print(row)

# Step 6: Close the connection
conn.close()
