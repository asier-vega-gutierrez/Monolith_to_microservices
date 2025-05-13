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
resource "azurerm_network_security_rule" "uvi_rule_http" {
  name                        = "uvi_rule_http"
  priority                    = 101
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "80"
  source_address_prefix       = "*"
  destination_address_prefix  = "10.0.6.5"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}