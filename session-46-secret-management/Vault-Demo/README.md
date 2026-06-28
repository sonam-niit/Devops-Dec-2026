# Vault for Secret Management in Terraform

- Valut is a tool for securely storing and accessing secrets like API keys, DB passwords, SSL certificates, encryption keys.
- for secret management we can use environment variable as well.
- export AWS_ACCESS_KEY_ID="your_AWS_ACCESS_KEY"
- use that in terraform

```tf
provider "aws" {
  access_key = var.AWS_ACCESS_KEY_ID
}
```

## Why vault instead of .env

- vault provides more security with encryption
- manage leaks (git commit)
- provides centralized access control
- supports dynamic secrets

## Let's work with Vault

[Vault Documentation](https://developer.hashicorp.com/vault/install)

```bash
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vault

# verify
vault help

# start vault server
vault server -dev
```
- after setting up vault server
- open another WSL to understand how to create secrets and access them.

```bash
export VAULT_ADDR='http://127.0.0.1:8200' # this is available  where vault is running

# create Secret
vault kv put secret/db-pass password='Sonam123'
# access secret
vault kv get secret/db-pass
```

## Access it in terraform

- create main.tf

```tf
provider "vault" {
  
}
data "vault_kv_secret" "db"{
    path = "secret/db-pass"
}
```

- create outputs.tf

```tf
output "database_password" {
  value = data.vault_kv_secret.db.data
  sensitive = true
}
```

- run below commands

```bash
terraform init
terraform apply --auto-approve
# you can see it can access password and showing sensitive
```

## Access valut with login 

- start vault server in one wsl terminal. if above one is already running then no need to start again. (vault server -dev)
- in anotrher terminal export address and then run command vault login
- it will ask for token: add that token from vault server
- it will be hidden so just paste and enter
- once you are authenticated.
- create new cred and try to access

```bash
vault kv put secret/cred username="admin" pass="admin123" # created multiple cred
vault kv get -format=json secret/cred # to read in JSON format
```

- trying to access.
- main.tf

```tf
provider "vault" {
  
}
data "vault_kv_secret_v2" "db"{
    mount = "secret"
    name = "cred"
}
```
- outputs.tf

```tf
output "database_password" {
  value = data.vault_kv_secret_v2.db.data["pass"]
  sensitive = true
}

output "database_username" {
  value = data.vault_kv_secret_v2.db.data["username"]
  sensitive = true
}
```

- terraform apply --auto-approve