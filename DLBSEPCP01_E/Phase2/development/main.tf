# -------------------------
# main.tf — Fully working without custom domain
# -------------------------

# 1️⃣ Set AWS Provider
provider "aws" {
  region = "us-east-1"
}

# 2️⃣  Create S3 Bucket for Static Website
resource "aws_s3_bucket" "website" {
  bucket = "fatima-ai-website-2026"
  force_destroy = true
}

# 3️⃣ Disable S3 Block Public Access for this bucket
resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket = aws_s3_bucket.website.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# 4️⃣ Set S3 Bucket Policy — allow public read
resource "aws_s3_bucket_policy" "public_read" {
  bucket = aws_s3_bucket.website.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = ["s3:GetObject"]
      Resource  = "${aws_s3_bucket.website.arn}/*"
    }]
  })
}

# 5️⃣ Configure S3 as a Static Website
resource "aws_s3_bucket_website_configuration" "website_config" {
  bucket = aws_s3_bucket.website.id
  index_document {
    suffix = "index.html"
  }
}

# 6️⃣ Upload index.html to S3
resource "aws_s3_object" "index" {
  bucket       = aws_s3_bucket.website.id
  key          = "index.html"
  source       = "index.html"
  content_type = "text/html"
}

# -------------------------
# Step 7 : CloudFront Distribution
# -------------------------
resource "aws_cloudfront_distribution" "website_cdn" {
  origin {
    domain_name = aws_s3_bucket.website.website_endpoint
    origin_id   = "s3-website-fatima-ai"

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "http-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "s3-website-fatima-ai"

    viewer_protocol_policy = "redirect-to-https"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }
viewer_certificate {
  cloudfront_default_certificate = true  # Use default CloudFront SSL (HTTPS)
}
  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  tags = {
    Name = "AI-Website-CDN"
  }
}
# -------------------------
# Step 8: Outputs
# -------------------------

output "cloudfront_url" {
  value       = "https://${aws_cloudfront_distribution.website_cdn.domain_name}"
  description = "The CloudFront distribution URL for the website"
}

output "s3_url" {
  value       = aws_s3_bucket_website_configuration.website_config.website_endpoint
  description = "The S3 website endpoint URL"
}

output "cloudfront_id" {
  value       = aws_cloudfront_distribution.website_cdn.id
  description = "The CloudFront distribution ID"
}