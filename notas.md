az account show
{
  "environmentName": "AzureCloud",
  "homeTenantId": "b5587048-a070-43ad-b654-20a31e9b2d99",
  "id": "16a94b55-2151-4fa9-8684-2ad3cd089429",
  "isDefault": true,
  "managedByTenants": [],
  "name": "Azure for Students",
  "state": "Enabled",
  "tenantDefaultDomain": "unedo365.onmicrosoft.com",
  "tenantDisplayName": "UNED",
  "tenantId": "b5587048-a070-43ad-b654-20a31e9b2d99",
  "user": {
    "name": "avega480@alumno.uned.es",
    "type": "user"
  }
}

## Chocolately
  (powershell como administrador)
  Get-ExecutionPolicy
  Set-ExecutionPolicy AllSigned
  Set-ExecutionPolicy Restricted


https://www.youtube.com/watch?v=V53AHWun17s&t=393s
## Terraform (https://registry.terraform.io/)
  terraform init
  terraform plan
  terraform apply -target 
  terraform apply -destroy
  terraform state list


## ssh
ssh-keygen -t rsa
C:\Users\asier/.ssh/azurekey
ssh -i ~/.ssh/azurekey adminasier@<public-ip>




# DNS zone
resource "azurerm_private_dns_zone" "dns_zone" {
  name                = "asiertxxo.com"
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
}

# Link the DNS zone to the virtual network
resource "azurerm_private_dns_zone_virtual_network_link" "dns_zone_vnl" {
  name                  = "test"
  resource_group_name   = azurerm_resource_group.asiertxxo_rg.name
  private_dns_zone_name = azurerm_private_dns_zone.dns_zone.name
  virtual_network_id    = azurerm_virtual_network.asiertxxo_vn.id
}

# DNS A Record for the VM
resource "azurerm_private_dns_a_record" "vm_record" {
  name                = "vm"  # Subdomain (e.g., vm.asiertxxo.com)
  zone_name           = azurerm_private_dns_zone.dns_zone.name
  resource_group_name = azurerm_resource_group.asiertxxo_rg.name
  ttl                 = 300
  records             = [azurerm_network_interface.asiertxxo_ni.private_ip_address]  # Pribate IP
}