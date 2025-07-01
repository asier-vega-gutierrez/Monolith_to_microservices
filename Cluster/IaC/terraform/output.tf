output "aks_id" {
  value = azurerm_kubernetes_cluster.cloud_cluster.id
}

output "aks_fqdn" {
  value = azurerm_kubernetes_cluster.cloud_cluster.fqdn
}

output "aks_node_rg" {
  value = azurerm_kubernetes_cluster.cloud_cluster.node_resource_group
}

output "acr_id" {
  value = azurerm_container_registry.cloud_registry.id
}

output "acr_login_server" {
  value = azurerm_container_registry.cloud_registry.login_server
}

resource "local_file" "kubeconfig" {
  depends_on   = [azurerm_kubernetes_cluster.cloud_cluster]
  filename     = "kubeconfig"
  content      = azurerm_kubernetes_cluster.cloud_cluster.kube_config_raw
}

output "mysql_disk_id" {
  value = azurerm_managed_disk.mysql_disk.id
}

output "sqls_disk_id" {
  value = azurerm_managed_disk.sqls_disk.id
}

output "postgres_disk_id" {
  value = azurerm_managed_disk.postgres_disk.id
}

output "influx_disk_id" {
  value = azurerm_managed_disk.influx_disk.id
}

