
# Public ip to know where to access
resource "azurerm_public_ip" "mysql_public_ip" {
  name                = "mysql_public_ip"
  resource_group_name = var.resource_group_name
  location            = var.resource_group_location
  allocation_method   = "Dynamic"
}

# Network interface to be able to use the public addres
resource "azurerm_network_interface" "mysql_ni" {
  name                = "mysql_ni"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Static"
    private_ip_address            = "10.0.2.6"
    public_ip_address_id          = azurerm_public_ip.mysql_public_ip.id
  }
}

# SSH public key to be able to access the virtual machine
resource "azurerm_ssh_public_key" "mysql_spk" {
  name                = "mysql_spk"
  resource_group_name = var.resource_group_name
  location            = "West Europe"
  public_key          = file("~/.ssh/azurekey.pub")
}

# Create a virtual machine with the created resources
resource "azurerm_virtual_machine" "mysql-vm" {
  name                  = "mysql-vm"
  location              = var.resource_group_location
  resource_group_name   = var.resource_group_name
  network_interface_ids = [azurerm_network_interface.mysql_ni.id]
  vm_size               = "Standard_B1ls" 
  
  delete_os_disk_on_termination = true
  delete_data_disks_on_termination = true

  storage_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  storage_os_disk {
    name              = "mysql_OSdisk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = "mysql-vm"
    admin_username = "adminasier"
    admin_password = "Admin1234!"
  }

  os_profile_linux_config {
    disable_password_authentication = true
    ssh_keys {
      path     = "/home/adminasier/.ssh/authorized_keys"
      key_data = azurerm_ssh_public_key.mysql_spk.public_key
    }
  }
}
