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

# Azure Bill of Materials (BoM) for Data Processing Solution

## Overview

This document details the Azure resources required for:
1. Fetching and processing files from the data lake container.
2. Integrating data from Oracle, Salesforce, and FTP sources.
3. Estimating costs for the Azure resources.

## Azure Resources

### 1. Data Lake Processing Resources

#### Azure Data Lake Storage Gen2 (ADLS)
- **Resource Type:** Storage Account
- **Name:** yourStorageAccountName
- **Location:** eastus
- **SKU:** Standard_LRS
- **Estimated Cost:** $x.xx per month

#### Azure Data Factory (ADF)
- **Resource Type:** Data Factory
- **Name:** yourDataFactoryName
- **Location:** eastus
- **Estimated Cost:** $x.xx per month

#### Azure SQL Database
- **Resource Type:** SQL Server and Database
- **Server Name:** yourSqlServerName
- **Database Name:** DataProcessingDB
- **Location:** eastus
- **Estimated Cost:** $x.xx per month

#### Azure Virtual Network (if required)
- **Resource Type:** Virtual Network
- **Name:** yourVNetName
- **Location:** eastus
- **Estimated Cost:** $x.xx per month

### 2. Data Integration Resources

#### Integration with Oracle
- **Resource Type:** Azure Data Factory (ADF)
  - **Name:** OracleDataFactory
  - **Location:** eastus
  - **Estimated Cost:** $x.xx per month

#### Integration with Salesforce
- **Resource Type:** Azure Data Factory (ADF)
  - **Name:** SalesforceDataFactory
  - **Location:** eastus
  - **Estimated Cost:** $x.xx per month

#### Integration with FTP
- **Resource Type:** Azure Data Factory (ADF)
  - **Name:** FTPDataFactory
  - **Location:** eastus
  - **Estimated Cost:** $x.xx per month

### Cost Estimation

Use the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to estimate the costs for the resources you will provision. Adjust the parameters based on your expected usage (e.g., data volume, frequency of data processing). Review the estimated monthly costs for the following:

- Storage Accounts: Add and configure the type of storage (e.g., Standard_LRS).
- SQL Database: Add and configure the SQL database (e.g., Single Database, DTU-based or vCore-based).
- Data Factory: Add and configure ADF (e.g., number of Data Factory operations).

## Data Lake Processing Steps

### Step 1: Provision Resources using ARM Template

1. Upload and deploy the `azure_resources.json` template via the Azure Portal.
2. Ensure all resources are provisioned successfully.

### Step 2: Configure SQL Database

1. Run the provided SQL scripts to set up the database and tables.
2. Ensure the database is configured correctly.

### Step 3: Set Up and Configure ADF for Data Lake Processing

1. Create pipelines for data ingestion and processing in Azure Data Factory.
2. Implement the following data processing steps:

#### Data Lake Processing Logic:

- **CUST_MSTR Files:**
  - Fetch files starting with "CUST_MSTR".
  - Extract date from filename and add it as a new column in the format `yyyy-MM-dd`.
  - Load the data into the `CUST_MSTR` table.

- **master_child_export Files:**
  - Fetch files starting with "master_child_export".
  - Extract date from filename and add it as new columns `Date` and `DateKey` in the formats `yyyy-MM-dd` and `yyyyMMdd` respectively.
  - Load the data into the `master_child` table.

- **H_ECOM_ORDER Files:**
  - Fetch files starting with "H_ECOM_ORDER".
  - Load the data into the `H_ECOM_Orders` table as is.

### Step 4: Run Data Processing Script

1. Use `data_processing.py` to process and load data into the SQL database.
2. Ensure the data processing script runs without errors.

## Data Integration Steps

### Step 1: Oracle Integration

1. Provision Azure Data Factory for Oracle integration.
2. Create pipelines to fetch incremental data from Oracle.
3. Load the data into the respective Azure SQL Database tables.

### Step 2: Salesforce Integration

1. Provision Azure Data Factory for Salesforce integration.
2. Create pipelines to fetch incremental data from Salesforce.
3. Load the data into the respective Azure SQL Database tables.

### Step 3: FTP Integration

1. Provision Azure Data Factory for FTP integration.
2. Create pipelines to fetch data from FTP.
3. Load the data into the respective Azure SQL Database tables.


