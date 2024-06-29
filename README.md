# Data-Engineering-Week-7-Assignment


# Azure Bill of Materials Solution

This repository contains the solution for creating an Azure Bill of Materials (BoM) for the given data processing requirements.


## Overview

The solution involves:
1. Storing raw data files from different sources in Azure Data Lake Storage (ADLS) Gen2.
2. Using Azure Data Factory (ADF) to orchestrate data movement and transformation.
3. Loading processed data into Azure SQL Database.

## Steps

### 1. Provision Azure Resources

Provision the necessary Azure resources using the ARM template (`azure_resources.json`):

1. Go to the [Azure Portal](https://portal.azure.com/).
2. Navigate to "Resource groups" and create a new resource group (e.g., `data-processing-rg`).
3. Navigate to "Deploy a custom template" and upload the `azure_resources.json` file.
4. Review and create the resources.

### 2. Set Up SQL Database and Tables

1. Open SQL Server Management Studio (SSMS).
2. Connect to your SQL Server instance.
3. Execute the `sql/create_database.sql` script to create the database.
4. Execute the `sql/create_tables.sql` script to create the necessary tables.

### 3. Configure Azure Data Factory

1. In the Azure Portal, navigate to the newly created Data Factory.
2. Create pipelines to:
   - Copy data from Oracle, Salesforce, and FTP to ADLS.
   - Transform and load data into Azure SQL Database.

