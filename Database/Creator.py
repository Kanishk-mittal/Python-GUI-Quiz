import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

def create():
    """
    This function will create a database named quiz_system and will create tables for each csv file in the data folder.
    for this it will load csv files and insert each file as a table with the same name in the database using pandas.
    This function assumes that there is no such database with the name quiz_system and the data folder contains csv files.
    """
    load_dotenv()
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    engine = create_engine(f"mysql+pymysql://root:{SQL_PASSWORD}@localhost")
    
    with engine.connect() as conn:
        from sqlalchemy import text
        conn.execute(text("CREATE DATABASE IF NOT EXISTS quiz_system"))
    
    engine = create_engine(f"mysql+pymysql://root:{SQL_PASSWORD}@localhost/quiz_system")
    
    for file in os.listdir("Database/DummyData"):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            df = pd.read_csv(f"Database/DummyData/{file}")
            df.to_sql(table_name, engine, if_exists="replace", index=False)

if __name__ == "__main__":
    create()
