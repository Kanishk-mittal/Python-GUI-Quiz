import pandas as pd
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

def create():
    """
    Creates a MySQL database named 'quiz_system' if it does not already exist,
    and populates it with tables from CSV files located in the 'Database/DummyData' directory.
    The function performs the following steps:
    1. Loads environment variables from a .env file.
    2. Retrieves the SQL password from the environment variables.
    3. Connects to the MySQL server using the retrieved password.
    4. Creates the 'quiz_system' database if it does not already exist.
    5. Connects to the 'quiz_system' database.
    6. Iterates through all CSV files in the 'Database/DummyData' directory.
    7. For each CSV file, creates or replaces a table in the 'quiz_system' database
       with the same name as the CSV file (excluding the file extension), and populates
       the table with data from the CSV file.
    Raises:
        FileNotFoundError: If the 'Database/DummyData' directory does not exist.
        KeyError: If the 'SQL_PASSWORD' environment variable is not set.
        sqlalchemy.exc.SQLAlchemyError: If there is an error connecting to the MySQL server
                                        or executing SQL commands.
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
