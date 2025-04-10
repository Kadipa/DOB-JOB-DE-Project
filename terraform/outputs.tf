output "s3_bucket_name" {
  value = aws_s3_bucket.data_lake_bucket.bucket
}

output "redshift_endpoint" {
  value = aws_redshiftserverless_workgroup.dob_redshift_workgroup.endpoint[0].address
}

output "iam_role_redshift_s3_access_arn" {
  value = aws_iam_role.redshift_s3_access_role.arn
}

output "glue_database_name" {
  value = aws_glue_catalog_database.dob_database.name
}

output "glue_crawler_name" {
  value = aws_glue_crawler.dob_crawler.name
}
