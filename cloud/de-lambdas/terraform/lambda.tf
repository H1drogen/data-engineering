
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_lambda_permission" "allow-s3" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.roll_dice.function_name
  principal = "s3.amazonaws.com"
  source_arn = "arn:aws:s3:::mybucket20240718102437846400000001"
  source_account = "471112635050"
}

resource "aws_iam_policy" "policy_one" {
  name = "policy-38966"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:GetObject",
                    "s3:GetObjectAcl",
                    "s3:DeleteObject"]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_policy" "policy_two" {
  name = "policy-381926"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:ListAllMyBuckets", "s3:ListBucket", "s3:HeadBucket"]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}


resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
  managed_policy_arns = [aws_iam_policy.policy_one.arn, aws_iam_policy.policy_two.arn]
}

# data "archive_file" "lambda" {
#   type        = "zip"
#   source_file = "/Users/simonh/northcoders/cloud/de-lambdas/lambda_functions/roll_dice"
#   output_path = "lambda_function_payload.zip"
# }

resource "aws_lambda_function" "roll_dice" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "roll_dice.zip"
  function_name = "roll_dice"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda_function.lambda_handler"

#   source_code_hash = data.archive_file.lambda.output_base64sha256
  runtime = "python3.12"

#   environment {
#     variables = {
#       foo = "bar"
#     }
  }

resource "aws_lambda_function" "save_monster" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "save_monster.zip"
  function_name = "save_monster"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda_function.lambda_handler"

  runtime = "python3.12"

  }