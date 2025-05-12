# Rules
resource "azurerm_network_security_rule" "db_rule_ssh" {
  name                        = "db_rule_ssh"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = "10.0.10.0/24"
  destination_address_prefix  = "10.0.1.0/24"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "db_rule_msql_output" {
  name                        = "db_rule_msql_output"
  priority                    = 101
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "3306"
  destination_port_range      = "3306"
  source_address_prefix       = "10.0.1.0/24"
  destination_address_prefix  = "10.0.2.6"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "db_rule_sqlserver_output" {
  name                        = "db_rule_sqlserver_output"
  priority                    = 102
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "1433"
  destination_port_range      = "1433"
  source_address_prefix       = "10.0.1.0/24"
  destination_address_prefix  = "10.0.2.7"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}




resource "azurerm_network_security_rule" "db_rule_postgres_output" {
  name                        = "db_rule_postgres_output"
  priority                    = 105
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "5432"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "db_rule_postgres_input" {
  name                        = "db_rule_postgres_input"
  priority                    = 106
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "5432"
  source_address_prefix       = "*"
  destination_address_prefix  = "10.0.1.5"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "db_rule_influxdb_output" {
  name                        = "db_rule_influxdb_output"
  priority                    = 107
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "8086"
  destination_port_range      = "*"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
resource "azurerm_network_security_rule" "db_rule_influxdb_input" {
  name                        = "db_rule_influxdb_input"
  priority                    = 108
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "*"
  source_port_range           = "*"
  destination_port_range      = "8086"
  source_address_prefix       = "*"
  destination_address_prefix  = "10.0.1.5"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}