provider "vault" {
  
}
# data "vault_kv_secret" "db"{
#     path = "secret/cred"
# }

data "vault_kv_secret_v2" "db"{
    mount = "secret"
    name = "cred"
}

