# The parameter $1 is the storage account key, which is passed when running the script.

# Blobs
az storage blob upload-batch --source DB/generation_files/mysql/ --destination container-mysql \
    --account-name cloudclustersa \
    --account-key $1 

az storage blob upload-batch --source PDagents/generation_files/data/ --destination container-pdagent-file \
    --account-name cloudclustersa \
    --account-key $1


# File shares
az storage file upload-batch  --source DB/generation_files/sqls/data --destination https://cloud_cluster_sa.file.core.windows.net/sqls-data \
    --account-name cloudclustersa \
    --account-key $1 
    
az storage file upload-batch --source DB/generation_files/sqls/log --destination https://cloud_cluster_sa.file.core.windows.net/sqls-log \
    --account-name cloudclustersa \
    --account-key $1 \
     
az storage file upload-batch  --source DB/generation_files/sqls/secrets --destination https://cloud_cluster_sa.file.core.windows.net/sqls-secrets \
    --account-name cloudclustersa \
    --account-key $1 \

az storage file upload-batch  --source DB/generation_files/postgres/data --destination https://cloud_cluster_sa.file.core.windows.net/postgres-data \
    --account-name cloudclustersa \
    --account-key $1 \

az storage file upload-batch  --source DB/generation_files/influx/data --destination https://cloud_cluster_sa.file.core.windows.net/influx-data \
    --account-name cloudclustersa \
    --account-key $1 \

az storage file upload-batch  --source DB/generation_files/influx/config --destination https://cloud_cluster_sa.file.core.windows.net/influx-config \
    --account-name cloudclustersa \
    --account-key $1 \

