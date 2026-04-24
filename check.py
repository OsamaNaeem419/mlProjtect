import pandas as pd
from sqlalchemy import create_engine

def db_to_file_and_read():
    # DB connection
    USER = "root"
    PASSWORD = "Proto786zoa!"
    HOST = "localhost"
    PORT = 3306
    DATABASE = "college"

    engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

    # Step 1: Read from DB (CHANGE table name if needed)
    df = pd.read_sql("SELECT * FROM student", con=engine)

    # Step 2: Save to new CSV file
    file_path = "output.csv"
    df.to_csv(file_path, index=False)

    # Step 3: Read that file again
    df_new = pd.read_csv(file_path)

    # Step 4: Show first 5 rows
    print(df_new.head())

if __name__ == "__main__":
    db_to_file_and_read()