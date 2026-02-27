variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "S3 bucket name"
  type        = string
  default     = "fatima-ai-website-2026"
}

variable "project_name" {
  description = "Project tag name"
  type        = string
  default     = "AI-Website-CDN"
}

variable "index_document" {
  description = "Main index file name"
  type        = string
  default     = "index.html"
}

variable "origin_id" {
  description = "CloudFront origin ID"
  type        = string
  default     = "s3-website-fatima-ai"
}