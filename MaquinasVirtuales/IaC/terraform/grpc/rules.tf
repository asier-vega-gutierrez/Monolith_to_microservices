# Rules
resource "azurerm_network_security_rule" "grcp_rule_ssh" {
  name                        = "grcp_rule_ssh"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = "10.0.10.0/24"
  destination_address_prefix  = "10.0.3.0/24"
  resource_group_name         = var.resource_group_name
  network_security_group_name = var.network_security_group_name
}
