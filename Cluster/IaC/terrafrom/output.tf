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