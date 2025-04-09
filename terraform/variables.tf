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
