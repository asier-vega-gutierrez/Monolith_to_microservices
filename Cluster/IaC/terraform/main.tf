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

# Cuennta de almacenamiento
resource "azurerm_storage_account" "cloud_cluster_sa" {
  name                     = "cloudclustersa"
  resource_group_name      = azurerm_resource_group.cloud_rg.name
  location                 = azurerm_resource_group.cloud_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# all continers
resource "azurerm_storage_container" "container_mysql" {
  name                  = "container-mysql"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}
resource "azurerm_storage_container" "container_influx" {
  name                  = "container-influx"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}
resource "azurerm_storage_container" "container_postgres" {
  name                  = "container-postgres"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}
resource "azurerm_storage_container" "container_sqls" {
  name                  = "container-sqls"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}
resource "azurerm_storage_container" "container_zookeeper" {
  name                  = "container-zookeeper"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}
resource "azurerm_storage_container" "container_pdagent_file" {
  name                  = "container-pdagent-file"
  storage_account_id    = azurerm_storage_account.cloud_cluster_sa.id
  container_access_type = "private"
}


# all blobs
resource "azurerm_storage_blob" "blob_mysql" {
  name                   = "blob_mysql"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_mysql.name
  type                   = "Block"
}
resource "azurerm_storage_blob" "blob_influx" {
  name                   = "blob_influx"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_influx.name
  type                   = "Block"
}
resource "azurerm_storage_blob" "blob_postgres" {
  name                   = "blob_postgres"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_postgres.name
  type                   = "Block"
}
resource "azurerm_storage_blob" "blob_sqls" {
  name                   = "blob_sqls"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_sqls.name
  type                   = "Block"
}
resource "azurerm_storage_blob" "blob_zookeeper" {
  name                   = "blob_zookeeper"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_zookeeper.name
  type                   = "Block"
}
resource "azurerm_storage_blob" "blob_pdagent_file" {
  name                   = "blob_pdagent_file"
  storage_account_name   = azurerm_storage_account.cloud_cluster_sa.name
  storage_container_name = azurerm_storage_container.container_pdagent_file.name
  type                   = "Block"
}