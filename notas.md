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
  terraform apply -target='module.cq'


## ssh
ssh-keygen -t rsa
C:\Users\asier/.ssh/azurekey
ssh -i ~/.ssh/azurekey adminasier@10.0.1.5

# ssh-agent
ssh-agent
*Copiar pegar en un shell lo que saca
ssh-add ~/ssh/azurekey
ssh-add -l 
ssh -A -i ~/.ssh/azurekey adminasier@13.81.0.82
ssh adminasier@10.0.1.5

# git
git reset --hard HEAD
