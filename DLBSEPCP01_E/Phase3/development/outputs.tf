output "cloudfront_url" {
  description = "CloudFront URL"
  value       = "https://${aws_cloudfront_distribution.website_cdn.domain_name}"
}

output "s3_url" {
  description = "S3 Website URL"
  value       = aws_s3_bucket_website_configuration.website_config.website_endpoint
}

output "cloudfront_id" {
  description = "CloudFront Distribution ID"
  value       = aws_cloudfront_distribution.website_cdn.id
}