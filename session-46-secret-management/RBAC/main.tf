resource "aws_iam_user" "developer" {
  name = "developer"
}

resource "aws_iam_policy" "s3_readonly" {
  name = "S3ReadOnlyPolicy"
  policy = jsonencode({
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Statement1",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
})
}

resource "aws_iam_user_policy_attachment" "attach" {
  user = aws_iam_user.developer.name
  policy_arn = aws_iam_policy.s3_readonly.arn
}

# Create IAM Group: developers
# Add above user to that group
# attach policy to that group

# Create Role
# attach policy to that role