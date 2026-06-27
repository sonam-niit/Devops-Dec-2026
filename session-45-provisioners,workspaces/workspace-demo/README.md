# Creating Workspace

- keep multiple environments isolated using same code files we can use workspace.

```bash
mkdir workspace-demo
cd workspace-demo

terraform init
terraform workspace new dev
#  create dev denvironment and switched to it
terraform workspace new prod
#  create prod denvironment and switched to it
terraform workspace list
# check state folder you can see seperate folder created for dev and prod both
```
- now create codes
- main.tf, variables.tf, outputs.tf
- now for seperate variables create tfvars file for both environments
- create folder tfvars
    - create prod.tfvars (add value)
    - create dev.tfvars (add value)

```bash
terraform workspace list
# check you are on dev workspace if not
terraform workspace select dev
terraform apply -var-file="tfvars/dev.tfvars" --auto-approve

terraform workspace select prod
terraform apply -var-file="tfvars/prod.tfvars" --auto-approve

# to destroy follow the same process
terraform workspace select dev
terraform destroy -var-file="tfvars/dev.tfvars" --auto-approve

terraform workspace select prod
terraform destroy -var-file="tfvars/prod.tfvars" --auto-approve
```