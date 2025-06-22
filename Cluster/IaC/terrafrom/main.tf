# Grupo de recursos
resource "azurerm_resource_group" "cloud_rg" {
  name     = var.resource_group_name
  location = var.location
}

# Esto es para permitir que el cluster pueda acceder y descargar del registry
resource "azurerm_role_assignment" "role_acrpull" {
  scope                            = azurerm_container_registry.cloud_registry.id
  role_definition_name             = "AcrPull"
  principal_id                     = azurerm_kubernetes_cluster.cloud_cluster.kubelet_identity.0.object_id
  skip_service_principal_aad_check = true
}

# Registry donde se subiran las imagenes
resource "azurerm_container_registry" "cloud_registry" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.cloud_rg.name
  location            = var.location
  sku                 = "Standard"
  admin_enabled       = true
}

# Cluster de kubenetes
resource "azurerm_kubernetes_cluster" "cloud_cluster" {
  name                = var.cluster_name
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
  dns_prefix          = "exampleaks1"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "standard_b2ms"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
  }
}