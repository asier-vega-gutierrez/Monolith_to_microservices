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
resource "azurerm_resource_group" "asiertxxo_rg" {
  name     = "asiertxxo_rg"
  location = "West Europe"
  tags = {
    enviroment = "dev"
  }
}

# Virtual network to manages ip of the resource group
resource "azurerm_virtual_network" "asiertxxo_vn" {
  name                = "asiertxxo_vn"
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
  location            = azurerm_resource_group.asiertxxo_rg.location
  address_space       = ["10.0.0.0/16"]
  tags = {
    enviroment = "dev"
  }
}

# Subnets to mannage diferent ip ranges
resource "azurerm_subnet" "asiertxxo_s1" {
  name                 = "asiertxxo_vn1"
  resource_group_name  = azurerm_resource_group.asiertxxo_rg.name
  virtual_network_name = azurerm_virtual_network.asiertxxo_vn.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Security group that cotains all network rules
resource "azurerm_network_security_group" "asiertxxo_nsg" {
  name                = "acceptanceTestSecurityGroup1"
  location            = azurerm_resource_group.asiertxxo_rg.location
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
  tags = {
    enviroment = "dev"
  }
}

# Asociate subnet to network security group
resource "azurerm_subnet_network_security_group_association" "asiertxxo_snsga" {
  subnet_id                 = azurerm_subnet.asiertxxo_s1.id
  network_security_group_id = azurerm_network_security_group.asiertxxo_nsg.id
}

# Rule: only developers with that ip can acces
resource "azurerm_network_security_rule" "asiertxxo_nsgr_dev" {
  name                        = "asiertxxo_nsgr_dev"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.asiertxxo_rg.name
  network_security_group_name = azurerm_network_security_group.asiertxxo_nsg.name
}

# Public ip to know where to access
resource "azurerm_public_ip" "asiertxxo_ip" {
  name                = "asiertxxo_ip"
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
  location            = azurerm_resource_group.asiertxxo_rg.location
  allocation_method   = "Dynamic"
  tags = {
    environment = "dev"
  }
}

# Network interface to be able to use the public addres
resource "azurerm_network_interface" "asiertxxo_ni" {
  name                = "asiertxxo_ni"
  location            = azurerm_resource_group.asiertxxo_rg.location
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.asiertxxo_s1.id
    private_ip_address_allocation = "Static"
    private_ip_address            = "10.0.1.5"
    public_ip_address_id          = azurerm_public_ip.asiertxxo_ip.id
  }
  tags = {
    environment = "dev"
  }
}

# SSH public key to be able to access the virtual machine
resource "azurerm_ssh_public_key" "admin_spk" {
  name                = "admin_spk"
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
  location            = "West Europe"
  public_key          = file("~/.ssh/azurekey.pub")
}

# Create a virtual machine with the created resources
resource "azurerm_virtual_machine" "asiertxxo-vm" {
  name                  = "asiertxxo-vm"
  location              = azurerm_resource_group.asiertxxo_rg.location
  resource_group_name   = azurerm_resource_group.asiertxxo_rg.name
  network_interface_ids = [azurerm_network_interface.asiertxxo_ni.id]
  vm_size               = "Standard_B2s" 
  
  delete_os_disk_on_termination = true
  delete_data_disks_on_termination = true

  storage_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  storage_os_disk {
    name              = "myosdisk1"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = "asiertxxo-vm"
    admin_username = "testadmin"
    admin_password = "Password1234!"
  }

  os_profile_linux_config {
    disable_password_authentication = true
    ssh_keys {
      path     = "/home/testadmin/.ssh/authorized_keys"
      key_data = azurerm_ssh_public_key.admin_spk.public_key
    }
  }

  tags = {
    environment = "dev"
  }
}
