variable "aws_region" {
  description = "AWS Region for resources"
  default     = "ap-southeast-1"
}

variable "s3_bucket_name" {
  description = "Unique bucket name for data lake"
}

variable "redshift_namespace" {
  description = "Namespace name for Redshift"
  default     = "dobnamespace"
}

variable "redshift_username" {
  description = "Redshift admin username"
}

variable "redshift_password" {
  description = "Redshift admin user password"
}

variable "redshift_db_name" {
  description = "Redshift database name"
  default     = "dobdb"
}

variable "glue_database_name" {
  description = "The name of the Glue catalog database."
  type        = string
  default     = "dob-db-glue-redshift"
}

variable "glue_crawler_name" {
  description = "The name of the Glue crawler."
  type        = string
  default     = "dob_jobs_crawler"
}

variable "s3_bucket_path" {
  description = "The S3 path where raw data is stored."
  type        = string
  default     = "s3://de-project-s3-datalake-bucket-south-east-region/dob_jobs/nyc_dob_job_data"
}

variable "iam_role" {
  description = "IAM role ARN used by Glue and Redshift Spectrum."
  type        = string
  default     = "arn:aws:iam::354294457076:role/RedshiftSpectrumRole"
}
