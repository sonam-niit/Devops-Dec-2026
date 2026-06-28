output "database_password" {
  value = data.vault_kv_secret_v2.db.data["pass"]
  sensitive = true
}

output "database_username" {
  value = data.vault_kv_secret_v2.db.data["username"]
  sensitive = true
}