import dlt
import pandas as pd

@dlt.resource(write_disposition="replace")
def nyc_dob_job_data():
    url = "https://data.cityofnewyork.us/resource/ic3t-wcy2.csv?$limit=50000"
    df = pd.read_csv(url, dtype=str)
    yield df

pipeline = dlt.pipeline(
    pipeline_name="nyc_dob_job_pipeline",
    destination="filesystem",
    dataset_name="dob_jobs"
)

pipeline.run(nyc_dob_job_data())
