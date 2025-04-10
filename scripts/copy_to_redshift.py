import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Load Redshift connection and schema info
host = os.getenv("REDSHIFT_HOST")
port = os.getenv("REDSHIFT_PORT")
dbname = os.getenv("REDSHIFT_DB")
user = os.getenv("REDSHIFT_USER")
password = os.getenv("REDSHIFT_PASSWORD")
target_schema = os.getenv("REDSHIFT_SCHEMA")
external_schema = os.getenv("SPECTRUM_SCHEMA")
external_table = os.getenv("SPECTRUM_TABLE")
target_table = os.getenv("REDSHIFT_TABLE")
iam_role = os.getenv("IAM_ROLE")

# Connect to Redshift
conn = psycopg2.connect(
    host=host, port=port, dbname=dbname, user=user, password=password
)
conn.set_session(autocommit=True)
cur = conn.cursor()

print(iam_role, "test")

# Create target Redshift table
cur.execute(f"""
CREATE TABLE IF NOT EXISTS "{target_schema}"."{target_table}" (
    "job" VARCHAR(65535),
    "doc" VARCHAR(65535),
    "borough" VARCHAR(65535),
    "house" VARCHAR(65535),
    "street_name" VARCHAR(65535),
    "block" VARCHAR(65535),
    "lot" VARCHAR(65535),
    "bin" VARCHAR(65535),
    "job_type" VARCHAR(65535),
    "job_status" VARCHAR(65535),
    "job_status_descrp" VARCHAR(65535),
    "latest_action_date" VARCHAR(65535),
    "building_type" VARCHAR(65535),
    "community___board" VARCHAR(65535),
    "cluster" VARCHAR(65535),
    "landmarked" VARCHAR(65535),
    "adult_estab" VARCHAR(65535),
    "loft_board" VARCHAR(65535),
    "city_owned" VARCHAR(65535),
    "little_e" VARCHAR(65535),
    "pc_filed" VARCHAR(65535),
    "efiling_filed" VARCHAR(65535),
    "plumbing" VARCHAR(65535),
    "mechanical" VARCHAR(65535),
    "boiler" VARCHAR(65535),
    "fuel_burning" VARCHAR(65535),
    "fuel_storage" VARCHAR(65535),
    "standpipe" VARCHAR(65535),
    "sprinkler" VARCHAR(65535),
    "fire_alarm" VARCHAR(65535),
    "equipment" VARCHAR(65535),
    "fire_suppression" VARCHAR(65535),
    "curb_cut" VARCHAR(65535),
    "other" VARCHAR(65535),
    "other_description" VARCHAR(65535),
    "applicant_s_first_name" VARCHAR(65535),
    "applicant_s_last_name" VARCHAR(65535),
    "applicant_professional_title" VARCHAR(65535),
    "applicant_license" VARCHAR(65535),
    "professional_cert" VARCHAR(65535),
    "pre__filing_date" VARCHAR(65535),
    "paid" VARCHAR(65535),
    "fully_paid" VARCHAR(65535),
    "assigned" VARCHAR(65535),
    "approved" VARCHAR(65535),
    "fully_permitted" VARCHAR(65535),
    "initial_cost" VARCHAR(65535),
    "total_est__fee" VARCHAR(65535),
    "fee_status" VARCHAR(65535),
    "existing_zoning_sqft" VARCHAR(65535),
    "proposed_zoning_sqft" VARCHAR(65535),
    "horizontal_enlrgmt" VARCHAR(65535),
    "vertical_enlrgmt" VARCHAR(65535),
    "enlargement_sq_footage" VARCHAR(65535),
    "street_frontage" VARCHAR(65535),
    "existingno_of_stories" VARCHAR(65535),
    "proposed_no_of_stories" VARCHAR(65535),
    "existing_height" VARCHAR(65535),
    "proposed_height" VARCHAR(65535),
    "existing_dwelling_units" VARCHAR(65535),
    "proposed_dwelling_units" VARCHAR(65535),
    "existing_occupancy" VARCHAR(65535),
    "proposed_occupancy" VARCHAR(65535),
    "site_fill" VARCHAR(65535),
    "zoning_dist1" VARCHAR(65535),
    "zoning_dist2" VARCHAR(65535),
    "zoning_dist3" VARCHAR(65535),
    "special_district_1" VARCHAR(65535),
    "special_district_2" VARCHAR(65535),
    "owner_type" VARCHAR(65535),
    "non_profit" VARCHAR(65535),
    "owner_s_first_name" VARCHAR(65535),
    "owner_s_last_name" VARCHAR(65535),
    "owner_s_business_name" VARCHAR(65535),
    "owner_s_house_number" VARCHAR(65535),
    "owner_shouse_street_name" VARCHAR(65535),
    "cityx" VARCHAR(65535),
    "state" VARCHAR(65535),
    "zip" VARCHAR(65535),
    "owner_sphone" VARCHAR(65535),
    "job_description" VARCHAR(65535),
    "dobrundate" VARCHAR(65535),
    "job_s1_no" VARCHAR(65535),
    "total_construction_floor_area" VARCHAR(65535),
    "withdrawal_flag" VARCHAR(65535),
    "signoff_date" VARCHAR(65535),
    "special_action_status" VARCHAR(65535),
    "special_action_date" VARCHAR(65535),
    "building_class" VARCHAR(65535),
    "job_no_good_count" VARCHAR(65535),
    "gis_latitude" VARCHAR(65535),
    "gis_longitude" VARCHAR(65535),
    "gis_council_district" VARCHAR(65535),
    "gis_census_tract" VARCHAR(65535),
    "gis_nta_name" VARCHAR(65535),
    "gis_bin" VARCHAR(65535)
);
""")

# Optional: truncate table before inserting
cur.execute(f'TRUNCATE TABLE "{target_schema}"."{target_table}";')

# Define columns and trim all to 256 chars
columns = [
    "job", "doc", "borough", "house", "street_name", "block", "lot", "bin",
    "job_type", "job_status", "job_status_descrp", "latest_action_date", "building_type",
    "community___board", "cluster", "landmarked", "adult_estab", "loft_board", "city_owned",
    "little_e", "pc_filed", "efiling_filed", "plumbing", "mechanical", "boiler", "fuel_burning",
    "fuel_storage", "standpipe", "sprinkler", "fire_alarm", "equipment", "fire_suppression",
    "curb_cut", "other", "other_description", "applicant_s_first_name", "applicant_s_last_name",
    "applicant_professional_title", "applicant_license", "professional_cert",
    "pre__filing_date", "paid", "fully_paid", "assigned", "approved", "fully_permitted",
    "initial_cost", "total_est__fee", "fee_status", "existing_zoning_sqft",
    "proposed_zoning_sqft", "horizontal_enlrgmt", "vertical_enlrgmt",
    "enlargement_sq_footage", "street_frontage", "existingno_of_stories",
    "proposed_no_of_stories", "existing_height", "proposed_height",
    "existing_dwelling_units", "proposed_dwelling_units", "existing_occupancy",
    "proposed_occupancy", "site_fill", "zoning_dist1", "zoning_dist2", "zoning_dist3",
    "special_district_1", "special_district_2", "owner_type", "non_profit",
    "owner_s_first_name", "owner_s_last_name", "owner_s_business_name",
    "owner_s_house_number", "owner_shouse_street_name", "cityx", "state", "zip",
    "owner_sphone", "job_description", "dobrundate", "job_s1_no", "total_construction_floor_area",
    "withdrawal_flag", "signoff_date", "special_action_status", "special_action_date",
    "building_class", "job_no_good_count", "gis_latitude", "gis_longitude",
    "gis_council_district", "gis_census_tract", "gis_nta_name", "gis_bin"
]

# Create trimmed SELECT clause
select_clause = ",\n    ".join([f'LEFT("{col}", 256)' for col in columns])

# Insert from external Spectrum table
cur.execute(f"""
INSERT INTO "{target_schema}"."{target_table}"
SELECT
    {select_clause}
FROM "{external_schema}"."{external_table}";
""")

print(f" Data copied from {external_schema}.{external_table} to {target_schema}.{target_table}")
cur.close()
conn.close()
