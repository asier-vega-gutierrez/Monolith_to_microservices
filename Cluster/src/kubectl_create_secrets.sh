# The parameter $1 is the storage account key, which is passed when running the script.
# The parameter $2 is the registry key, which is passed when running the script.


kubectl create secret generic azure-storage-key \
  --from-literal=account-key=$1 \
  -n cloudnamespace

kubectl create secret generic azure-files-secret \
  --from-literal=azurestorageaccountname=cloudclustersa \
  --from-literal=azurestorageaccountkey=$1 \
  -n cloudnamespace

kubectl create secret docker-registry cloudregistryasier-credentials \
  --docker-server=cloudregistryasier.azurecr.io \
  --docker-username=cloudregistryasier \
  --docker-password=$2 \
  -n cloudnamespace