# Rules
resource "azurerm_network_security_rule" "loaders_rule_ssh" {
  name                        = "loaders_rule_ssh"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = "10.0.10.0/24"
  destination_address_prefix  = "10.0.4.0/24"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "loaders_rule_influx" {
  name                        = "loaders_rule_influx"
  priority                    = 101
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "8086"
  destination_port_range      = "8086"
  source_address_prefix       = "10.0.4.0/24"
  destination_address_prefix  = "10.0.1.0/24"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "loaders_rule_post" {
  name                        = "loaders_rule_post"
  priority                    = 102
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "5432"
  destination_port_range      = "5432"
  source_address_prefix       = "10.0.4.0/24"
  destination_address_prefix  = "10.0.1.0/24"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}