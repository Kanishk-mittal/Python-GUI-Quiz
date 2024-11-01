import mysql.connector as msc
import pandas as pd
import dotenv
import os

def create():
    """
    This function will create a database named quiz_system and will create tables for each csv file in the data folder.
    for this it will load csv files and insert each file as a table with the same name in the database using pandas.
    This function assumes that there is no such database with the name quiz_system and the data folder contains csv files.
    """
    os.load_dotenv()
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    conn = msc.connect(host="localhost", user="root", password=SQL_PASSWORD)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE quiz_system")
    conn.commit()
    cursor.close()
    conn.close()
    conn = msc.connect(host="localhost", user="root", password=SQL_PASSWORD, database="quiz_system")
    for file in os.listdir("Database/DummyData"):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            df = pd.read_csv(f"data/{file}")
            df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()