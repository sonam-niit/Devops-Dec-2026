# Remote Backend

- for managing state remotely create one s3 bucket: remote-backend-terraform-demo

- edit existing code of aws-sec

```tf
terraform {
  backend "s3" {
    bucket = "remote-backend-terraform-demo"
    key = "terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    # dynamodb_table = "mytable"
    # for state locking while collab
  }
}
```

- then again run command

```bash
terraform init
```

- it will change local backend to remote
- if you have already created earlier resources then it will ask do you want to copy old terraform.tfstate file from local to your s3 bucket.
- say yes and it will initialize new backend on s3 bucket.
- now if you run 

```bash
terraform destroy --auto-approve
```
- It will manage state remotely

- if you want to keep the code seperated like variables and output then you can create backend.tf file and just include code shown above that will also understand Its remote backend to configure while creating Infra.