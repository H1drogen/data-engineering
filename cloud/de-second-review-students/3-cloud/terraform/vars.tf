variable "data_bucket_prefix" {
  type    = string
  default = "nc-demo-de-quotes"
}


variable "code_bucket_prefix" {
  type    = string
  default = "nc-demo-de-code"
}

variable "lambda_name" {
  type    = string
  default = "quote_handler"
}

variable "python_runtime" {
  type    = string
  default = "python3.12"
}

variable "aws_log_group_name" {
  type    = string
  default = "/aws/lambda/quote_handler"
}
