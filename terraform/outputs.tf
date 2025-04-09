output "s3_bucket_name" {
  value = aws_s3_bucket.data_lake_bucket.bucket
}

output "redshift_endpoint" {
  value = aws_redshiftserverless_workgroup.dob_redshift_workgroup.endpoint[0].address
}

output "iam_role_redshift_s3_access_arn" {
  value = aws_iam_role.redshift_s3_access_role.arn
}
