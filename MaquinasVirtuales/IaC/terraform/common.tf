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

# Modules
module "db" {
  source = "./db"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
}
