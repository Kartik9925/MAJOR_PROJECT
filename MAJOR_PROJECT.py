
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from psycopg2 import sql
def process_scenario_1(db_parameters):
    df = pd.read_csv("Medical_det.csv")
    intv = int(input("Enter the number: "))
    
    if intv == 1:
        table_name = "patients_details2"
    else:
        table_name = "full_details2"
    conn = psycopg2.connect(**db_parameters)
    engine = create_engine(f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['database']}")
    
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    conn.close()
    if intv == 0:
        conn = psycopg2.connect(**db_parameters)
        with conn.cursor() as cursor:
            view_query = f"CREATE VIEW view_name AS SELECT NAME, ADDRESS FROM {table_name};"
            cursor.execute(view_query)
            conn.commit()
        conn.close()
    print(df)    

#SCENARIO 2
# APPLYING VIEW ON BLINDED FILE
def process_scenario_2(db_parameters):
    df = pd.read_csv("Medical_det.csv")
    conn = psycopg2.connect(**db_parameters)
    engine = create_engine(f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['database']}")
    
    df.to_sql("patients_details", con=engine, if_exists="replace", index=False)
    
    with conn.cursor() as cursor:
        create_view_sql = """
            CREATE OR REPLACE VIEW patients_details_view AS
            SELECT *
            FROM patients_details;
        """
        cursor.execute(create_view_sql)
        conn.commit()
    conn.close()
    print(df)


# Scenario 3
#APPLY MASKING ON CERTAIN COLUMNS AND HIDE GIVEN COLUMN
def process_scenario_3(db_parameters):
    def mask_data(data):
        return "xxxxxxxxxx"
    
    df = pd.read_csv("Pharma_data.csv")
    columns_to_mask = ["MOBILE_NUMBER"]
    
    for col in columns_to_mask:
        df[col] = df[col].apply(mask_data)
    
    conn = psycopg2.connect(**db_parameters)
    engine = create_engine(f"postgresql://{db_parameters['user']}:{db_parameters['password']}@{db_parameters['host']}:{db_parameters['port']}/{db_parameters['database']}")
    
    masked_df = df.drop(columns=columns_to_mask + ["NAME", "ADDRESS"])
    masked_df.to_sql("full_details3", con=engine, if_exists="replace", index=False)
    conn.close()   
    print(df) 
def main():
    db_parameters = {
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "kartik",
        "port": "9925"
    }
    scenario = int(input("Enter scenario (1, 2, or 3): "))
    
    if scenario == 1:
        process_scenario_1(db_parameters)
    elif scenario == 2:
        process_scenario_2(db_parameters)
    elif scenario == 3:
        process_scenario_3(db_parameters)
    else:
        print("Invalid scenario choice.")

if __name__ == "__main__":
    main()
