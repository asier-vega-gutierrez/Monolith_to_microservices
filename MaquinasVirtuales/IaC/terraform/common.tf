# Configure the Azure provider
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

# Resource group that cotains all the resources for the project
resource "azurerm_resource_group" "cloud_rg" {
  name     = "cloud_rg"
  location = "West Europe"
}

# Virtual network to manages ip of the resource group
resource "azurerm_virtual_network" "vn" {
  name                = "vn"
  resource_group_name = azurerm_resource_group.cloud_rg.name
  location            = azurerm_resource_group.cloud_rg.location
  address_space       = ["10.0.0.0/16"]
  depends_on = [ azurerm_resource_group.cloud_rg ]
}

# Subnet for the DB
resource "azurerm_subnet" "db_subnet" {
  name                 = "db_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.1.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "db_nsg" {
  name                = "db_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "db_nsg_association" {
  subnet_id                 = azurerm_subnet.db_subnet.id
  network_security_group_id = azurerm_network_security_group.db_nsg.id
}


# Subnet for the extractors
resource "azurerm_subnet" "extractors_subnet" {
  name                 = "extractors_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.2.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "extractors_nsg" {
  name                = "extractors_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "extractors_nsg_association" {
  subnet_id                 = azurerm_subnet.extractors_subnet.id
  network_security_group_id = azurerm_network_security_group.extractors_nsg.id
}


# Modules
module "db" {
  source = "./db"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.db_subnet.id
  network_security_group_name = azurerm_network_security_group.db_nsg.name
}
module "extractors" {
  source = "./extractors"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.extractors_subnet.id
  network_security_group_name = azurerm_network_security_group.extractors_nsg.name
}

