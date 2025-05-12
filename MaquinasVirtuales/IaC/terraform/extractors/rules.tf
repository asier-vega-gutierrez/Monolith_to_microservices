# Rules
resource "azurerm_network_security_rule" "extractors_rule_ssh" {
  name                        = "extractors_rule_ssh"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = "*"
  destination_address_prefix  = "10.0.2.5"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}

resource "azurerm_network_security_rule" "extractors_rule_grcp" {
  name                        = "grcp_rule_ssh"
  priority                    = 101
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "50051"
  destination_port_range      = "50051"
  source_address_prefix       = "10.0.2.0/24"
  destination_address_prefix  = "10.0.3.5"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}

resource "azurerm_network_security_rule" "extractors_rule_mysql" {
  name                        = "extractors_rule_mysql"
  priority                    = 102
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "3306"
  destination_port_range      = "3306"
  source_address_prefix       = "10.0.1.0/24"
  destination_address_prefix  = "10.0.2.6"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}

resource "azurerm_network_security_rule" "extractors_rule_sqls" {
  name                        = "extractors_rule_sqls"
  priority                    = 103
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "1433"
  destination_port_range      = "1433"
  source_address_prefix       = "10.0.1.0/24"
  destination_address_prefix  = "10.0.2.7"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}