import pandas as pd
import mysql.connector

# Step 1: Load the CSV file
df = pd.read_csv('products.csv')

# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Manoj@029',  # Use your actual password
    database='ecommerce'   # Make sure this DB exists
)

cursor = conn.cursor()

# Step 3: Create table (you can modify as needed based on your CSV)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INT,
        name VARCHAR(255),
        brand VARCHAR(100),
        category VARCHAR(100),
        price DECIMAL(10, 2),
        stock INT,
        description TEXT,
        image_url VARCHAR(255),
        rating FLOAT,
        sku VARCHAR(100)
    )
''')

# Step 4: Insert data (manually mapping CSV columns)
for index, row in df.iterrows():
    row = row.where(pd.notnull(row), None)
    cursor.execute('''
    INSERT INTO products (
        id, name, brand, category, cost, retail_price, department, sku, distribution_center_id
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''', (
    row['id'],
    row['name'],
    row['brand'],
    row['category'],
    row['cost'],
    row['retail_price'],
    row['department'],
    row['sku'],
    row['distribution_center_id']
))


# Step 5: Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded into MySQL successfully!")
