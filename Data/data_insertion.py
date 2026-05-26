import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Read CSV file
csv_file = 'shop-product-catalog.csv'
data = pd.read_csv(csv_file)

# Connect to MySQL
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=os.getenv("DB_PASSWORD"),
    database='shopassistent'
)

cursor = db_connection.cursor()

# Insert data
for index, row in data.iterrows():
    sql = """
    INSERT INTO Products 
    (ProductID, ProductName, ProductBrand, Gender, Price, Description, PrimaryColour)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(sql, tuple(row))

db_connection.commit()

cursor.close()
db_connection.close()

print("Data inserted successfully!")