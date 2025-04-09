import psycopg2
import os
from dotenv import load_dotenv

def create_external_schema():
    load_dotenv()

    host = os.getenv("REDSHIFT_HOST")
    port = os.getenv("REDSHIFT_PORT")
    dbname = os.getenv("REDSHIFT_DB")
    user = os.getenv("REDSHIFT_USER")
    password = os.getenv("REDSHIFT_PASSWORD")
    glue_database = os.getenv("GLUE_DATABASE_NAME")   # e.g., dob_db_glue_redshift
    external_schema = os.getenv("SPECTRUM_SCHEMA")     # usually same as glue DB
    region = os.getenv("AWS_DEFAULT_REGION")
    iam_role = os.getenv("IAM_ROLE")

    conn = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    print("trace", iam_role)

    # Create external schema if not exists
    cur.execute(f"""
    CREATE EXTERNAL SCHEMA IF NOT EXISTS "{external_schema}"
    FROM DATA CATALOG
    DATABASE '{glue_database}'
    IAM_ROLE '{iam_role}'
    REGION '{region}';
    """)

    print(f"External schema '{external_schema}' mapped to Glue DB '{glue_database}' created.")
    cur.close()
    conn.close()

