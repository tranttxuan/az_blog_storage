Steps to run
- az login
<!-- Create a resource group for the resources -->
- az group create --location <myLocation> --name az204-blob-rg #create
<!-- Create a storage account -->
<!-- storage account name should be unique -->
- az storage account create --resource-group az204-blob-rg --name <myStorageAcct> --location <francecentral> --sku Standard_LRS 
- get key 

