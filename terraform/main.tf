provider "aws" {
  region = var.aws_region
}

# S3 bucket as Data Lake
resource "aws_s3_bucket" "data_lake_bucket" {
  bucket = var.s3_bucket_name
}

# Redshift Serverless Namespace
resource "aws_redshiftserverless_namespace" "dob_redshift_namespace" {
  namespace_name      = var.redshift_namespace
  admin_username      = var.redshift_username
  admin_user_password = var.redshift_password
  db_name             = var.redshift_db_name
}

# Redshift Serverless Workgroup
resource "aws_redshiftserverless_workgroup" "dob_redshift_workgroup" {
  workgroup_name      = "${var.redshift_namespace}-workgroup"
  namespace_name      = aws_redshiftserverless_namespace.dob_redshift_namespace.namespace_name
  publicly_accessible = true

  config_parameter {
    parameter_key   = "max_query_execution_time"
    parameter_value = "3600"
  }
}

# IAM Role for Redshift to access S3
resource "aws_iam_role" "redshift_s3_access_role" {
  name = "redshift_s3_access_role_dob"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "redshift.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
}

# Attach S3 read policy to IAM role
resource "aws_iam_role_policy_attachment" "redshift_s3_policy_attachment" {
  role       = aws_iam_role.redshift_s3_access_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}


resource "aws_glue_catalog_database" "dob_database" {
  name = var.glue_database_name
}


resource "aws_glue_crawler" "dob_crawler" {
  name          = var.glue_crawler_name
  database_name = aws_glue_catalog_database.dob_database.name
  role          = aws_iam_role.redshift_spectrum_role.arn

  s3_target {
    path = var.s3_bucket_path
  }

  configuration = jsonencode({
    Version: 1.0,
    Grouping: {
      TableGroupingPolicy: "CombineCompatibleSchemas"
    }
  })
}

resource "aws_iam_role" "redshift_spectrum_role" {
  name = "RedshiftSpectrumRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = [
            "glue.amazonaws.com",
            "redshift.amazonaws.com"
          ]
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}
