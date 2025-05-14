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

#subnet for the jumpbox
resource "azurerm_subnet" "jumpbox_subnet" {
  name                 = "jumpbox_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.10.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "jumpbox_nsg" {
  name                = "jumpbox_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "jumpbox_nsg_association" {
  subnet_id                 = azurerm_subnet.jumpbox_subnet.id
  network_security_group_id = azurerm_network_security_group.jumpbox_nsg.id
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

# Subnet for the grcp
resource "azurerm_subnet" "grcp_subnet" {
  name                 = "grcp_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.3.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "grcp_nsg" {
  name                = "grcp_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "grcp_nsg_association" {
  subnet_id                 = azurerm_subnet.grcp_subnet.id
  network_security_group_id = azurerm_network_security_group.grcp_nsg.id
}

# Subnet for the uvi
resource "azurerm_subnet" "uvi_subnet" {
  name                 = "uvi_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.6.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "uvi_nsg" {
  name                = "uvi_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "uvi_nsg_association" {
  subnet_id                 = azurerm_subnet.uvi_subnet.id
  network_security_group_id = azurerm_network_security_group.uvi_nsg.id
}

# Subnet for the digital twin
resource "azurerm_subnet" "dt_subnet" {
  name                 = "dt_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.5.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "dt_nsg" {
  name                = "dt_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "dt_nsg_association" {
  subnet_id                 = azurerm_subnet.dt_subnet.id
  network_security_group_id = azurerm_network_security_group.dt_nsg.id
}

# Subnet for the loaders
resource "azurerm_subnet" "loaders_subnet" {
  name                 = "loaders_subnet"
  resource_group_name  = azurerm_resource_group.cloud_rg.name
  virtual_network_name = azurerm_virtual_network.vn.name
  address_prefixes     = ["10.0.4.0/24"]
}
# Security group that cotains all network rules
resource "azurerm_network_security_group" "loaders_nsg" {
  name                = "loaders_nsg"
  location            = azurerm_resource_group.cloud_rg.location
  resource_group_name = azurerm_resource_group.cloud_rg.name
}
# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "loaders_nsg_association" {
  subnet_id                 = azurerm_subnet.loaders_subnet.id
  network_security_group_id = azurerm_network_security_group.loaders_nsg.id
}


# Modules
module "jumpbox" {
  source = "./jumpbox"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.jumpbox_subnet.id
  network_security_group_name = azurerm_network_security_group.jumpbox_nsg.name
}
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
module "grpc" {
  source = "./grpc"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.grcp_subnet.id
  network_security_group_name = azurerm_network_security_group.grcp_nsg.name
}
module "uvi" {
  source = "./uvi"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.uvi_subnet.id
  network_security_group_name = azurerm_network_security_group.uvi_nsg.name
}
module "dt" {
  source = "./dt"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.dt_subnet.id
  network_security_group_name = azurerm_network_security_group.dt_nsg.name
}
module "loaders" {
  source = "./loaders"
  resource_group_name   = azurerm_resource_group.cloud_rg.name
  resource_group_location = azurerm_resource_group.cloud_rg.location
  virtual_network_name = azurerm_virtual_network.vn.name
  subnet_id = azurerm_subnet.loaders_subnet.id
  network_security_group_name = azurerm_network_security_group.loaders_nsg.name
}


