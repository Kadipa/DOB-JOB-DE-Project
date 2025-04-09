SELECT
  borough,
  job_type,
  COUNT(*) AS total_jobs
FROM {{ source('spectrum_schema', 'nyc_dob_jobs') }}
GROUP BY borough, job_type
