
resource "aws_cloudwatch_log_metric_filter" "yada" {
  name           = "GreatQuoteFilter"
  pattern        = "GREAT QUOTE"
  log_group_name = aws_lambda_function.quote_handler.logging_config

  metric_transformation {
    name      = "GreatQuoteMetric"
    namespace = "CustomLambdaMetrics"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "alarm" {
  alarm_name          = "GreatQuoteAlarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "GreatQuoteMetric"
  namespace           = "CustomLambdaMetrics"
  period              = 60
  threshold           = 1
  alarm_actions     = [aws_ses_event_destination.destination.arn]
}

resource "aws_ses_email_identity" "email" {
  email = "dataengineering@northcoders.com"
}

resource "aws_ses_configuration_set" "set" {
  name = "GreatQuoteConfigurationSet"
}

resource "aws_ses_event_destination" "destination" {
  name               = "GreatQuoteDestination"
  configuration_set_name = aws_ses_configuration_set.set.name
  enabled            = true
  matching_types     = ["bounce", "send"]
}





