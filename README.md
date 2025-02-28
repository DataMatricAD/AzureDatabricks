# AzureDatabricks

Azure Databricks Project (With ADF)


Resource Group and Resource Creation
1.	Create Azure Account (Pay As You Go Subscription) - Create Your Azure Free Account Or Pay As You Go | Microsoft Azure
   ![image](https://github.com/user-attachments/assets/7c1389fe-e124-4e58-b724-ea70fb0ba4e9)
 
Provide your email-address, credit card and other details to complete the signup process
 ![image](https://github.com/user-attachments/assets/9adba55d-c2c5-4c10-8bdd-819955fb786c)

2.	Now we should be able to login to Azure Portal
 ![image](https://github.com/user-attachments/assets/4166ea4a-3b3e-4044-a16d-61b7fe7d24ab)

3.	Create Resource Group
 
![image](https://github.com/user-attachments/assets/ca77e91f-5e72-42f7-90c4-4927a04110e1)
![image](https://github.com/user-attachments/assets/bb41ba85-9109-4f0b-b9b3-7f82eb5e1c8b)
![image](https://github.com/user-attachments/assets/828027d7-d2de-402e-bd62-cb07f53b1acb)


4.	Create Azure Synapse Analytics and Storage Account (ADLS Gen2)
   ![image](https://github.com/user-attachments/assets/a8e70476-a0b7-4555-8131-9f42540ce13b)

 
Synapse Analytics Workspace creation - > synapse-workspace-demo-dbs-01
Basic Page (work space details)
![image](https://github.com/user-attachments/assets/58ad3ee8-0a71-415e-83bf-e49b38123cc8)

 
Note: Make sure the "Assign myself the Storage Blob Data Contributor role on the Data Lake Storage Gen2 account to interactively query it in the workspace." check box is enabled.  This will make sure the Synapse Analytics have required access to the Storage account.

Security Page
![image](https://github.com/user-attachments/assets/74bc2cfa-6303-45cd-b4ce-4e84424dbfde)

Networking Page
![image](https://github.com/user-attachments/assets/659002bb-0461-409d-82aa-13aef69922e6)
![image](https://github.com/user-attachments/assets/2020f22a-972c-4fa7-8524-2971da4648a2)

Now review and create the resource.
![image](https://github.com/user-attachments/assets/6ead8bc2-868d-456c-afd5-332f88a462fc)
![image](https://github.com/user-attachments/assets/11e89763-87a4-4d84-b678-4249158c42d0)
![image](https://github.com/user-attachments/assets/6fb25b49-b233-4e0d-af18-59b4d06130e7)
![image](https://github.com/user-attachments/assets/99e96e66-900f-42c1-9bdf-a7b7048722f2)
![image](https://github.com/user-attachments/assets/a8dd746a-21ad-4878-8acc-6f631ab7e582)

After a success deployment, we can navigate to the resource.
![image](https://github.com/user-attachments/assets/07c6c5a1-99ae-44d2-a50c-f5e4e1f52cd9)

Use serverless endpoint to connect from SSMS (with MFA)
![image](https://github.com/user-attachments/assets/6d4c1331-49d3-4996-a81a-ee63b5290533)
![image](https://github.com/user-attachments/assets/2ed8f5d0-bde9-418b-a0e0-13c580e7d8eb)

5.	Create Azure Data Factory (ADF)
![image](https://github.com/user-attachments/assets/c5d37ac6-8a5a-4dd0-8218-cb2ae6d4ac62)

Basic Page
![image](https://github.com/user-attachments/assets/c02d2fea-4ccf-488c-bd50-f5b227b45f2c)

Git Configuration (for code deployment – CI/CD)
![image](https://github.com/user-attachments/assets/3db34ccb-ed8c-4157-9ecd-62e1df597b7d)

Networking Page
![image](https://github.com/user-attachments/assets/1afb32b7-397a-435c-8f77-c5d4f59e7194)

Advanced page for security and encryption
![image](https://github.com/user-attachments/assets/1ccb7eda-10da-44e0-a69a-60b9d45d535b)
![image](https://github.com/user-attachments/assets/df4295a9-ca14-4cb6-9c4f-7a9e1d495cf8)
 
Review and create resource.
![image](https://github.com/user-attachments/assets/e3cdeca9-4550-4d97-9045-9a3f7e9d0b27)
![image](https://github.com/user-attachments/assets/2d7dfc14-5881-4159-aea3-79832145204d)

After a successful deployment, we can verify the resource under the RG.
![image](https://github.com/user-attachments/assets/cc2a5a18-54d3-4036-81b2-362a2313885f)

6.	Create Azure Databricks Workspace 
Find Databricks in Azure Market Place and select create button.
![image](https://github.com/user-attachments/assets/767e961b-6ea9-4322-bc9e-21a3eb4cefa9)
 
Basic Page
We need to use Azure Pay As You Go subscription so we can select Premium (+ Role-based Access Control). Without Premium plan, we won’t be able to use Unity Catalog
![image](https://github.com/user-attachments/assets/d6cecc05-1b51-4006-8a99-8896fff8de38)

Networking (for enterprises and organizations – use virtual networks (VNets) with no public IP configurations).
![image](https://github.com/user-attachments/assets/cc5fb27a-632f-44c8-9004-0e429d300503)

Encryption Page
![image](https://github.com/user-attachments/assets/4bc0440e-c27f-49a9-9002-94995a923810)

Security and Compliance Page 
![image](https://github.com/user-attachments/assets/f6b85e6d-6bfc-461c-82fc-d46e77484338)
![image](https://github.com/user-attachments/assets/a9b74674-590f-491b-a92f-34308abbceca)

Review and Create the Databricks resource.
![image](https://github.com/user-attachments/assets/d52f794b-b42d-459a-8086-15cc9453b2c4)
![image](https://github.com/user-attachments/assets/edd29ef3-f9dc-47b9-a880-f23d4c95a9fa)
![image](https://github.com/user-attachments/assets/93ed7c45-6862-4ad3-905b-2bf2d0655dd8)
![image](https://github.com/user-attachments/assets/5eae8df3-1b72-4f1c-adbf-9fe0c20d4fbd)

After a successful deployment, we should be able to see the resource. We can launch workspace by clicking the Launch button or selecting the URL
![image](https://github.com/user-attachments/assets/5ac1e3f3-ea6e-4dcd-af47-cf4fd397e893)
![image](https://github.com/user-attachments/assets/73cbbefb-eb3c-4eaf-9251-7f75decdec6d)

7.	Azure Key Vault Creation
It is a cloud service used to securely store and manage sensitive information such as keys, secrets, and certificates. Its primary use case is to protect access to applications, services, and IT resources by centralizing credential management and ensuring secure access through role-based permissions.
![image](https://github.com/user-attachments/assets/2c3d06b0-1626-4201-adde-67bb312b272c)

Basic Page
![image](https://github.com/user-attachments/assets/e5eda8df-910c-49d2-939a-685d87e5c3b1)
 
Configure the options as per the below screenshot. (Note: In this course we are going with the "Vault Access Policy" Permission model, however it's not recommended currently).
![image](https://github.com/user-attachments/assets/27dd2af6-e67f-4aac-9033-47bc6b43841c)
![image](https://github.com/user-attachments/assets/1e0fce22-4919-47bd-be87-9cc5b375b645)
![image](https://github.com/user-attachments/assets/612e24c2-d08d-4df7-bf8d-1adb33a45301)
![image](https://github.com/user-attachments/assets/8230030d-02bf-479b-a33c-7c58b841c8b9)
![image](https://github.com/user-attachments/assets/6d809a5e-629c-4eff-b9dc-2d48071502ad)
![image](https://github.com/user-attachments/assets/11d3fb36-acfe-467d-b671-c6d48a457a6f)

8.	It is an additional step to load a sample database in SSMS. Setting up data source - https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks
![image](https://github.com/user-attachments/assets/6d035ae3-e9e0-4c5a-91d3-6b2f4c16f5fc)
![image](https://github.com/user-attachments/assets/fee9540f-27b7-4325-a533-f18902e4a5b3)

This user login will be used to setup SHIR in ADF. So we will be able to read on premise data and load to ADLS Gen2.
![image](https://github.com/user-attachments/assets/7b2868b3-93a3-4895-a114-4ef9602733de)
![image](https://github.com/user-attachments/assets/aa9e9842-35be-4d5b-92e7-84ebfdddafeb)
![image](https://github.com/user-attachments/assets/c167357e-27e1-4bb4-8e9e-1bb070c61a81)

9.	Data Ingestion Phase

First, we will launch ADF.
![image](https://github.com/user-attachments/assets/570faed8-db2f-44e0-ae9f-860d5cca58c2)

Creating a SHIR to connect to On Premise SQL Server (select Azure, Self-Hosted)
![image](https://github.com/user-attachments/assets/f293c3b1-4620-44a4-bb52-6a3a692f253e)

Select Self-Hosted
![image](https://github.com/user-attachments/assets/7dbb3b42-ac6d-43ff-aa71-efc7ef91f278)

Provide a name
![image](https://github.com/user-attachments/assets/d3f1a17b-0843-4448-87de-66472bec6684)

Use Express setup for local computer
![image](https://github.com/user-attachments/assets/aad6065c-dcf3-47be-843b-eb60e7b9c4d3)

Integration Runtime (Self-hosted) Express Setup will run in your local. We should be using either express or manual setup based on our client requirement.
![image](https://github.com/user-attachments/assets/fe92dac3-5521-4534-b44e-01ac7d382c45)
![image](https://github.com/user-attachments/assets/a5a11a5b-fa5a-4424-974d-6b3c391f91de)

After a success installation, we should be able to see the Self Hosted Integration Runtime under Integration Runtime. And it is ready to use.
![image](https://github.com/user-attachments/assets/814410fb-84ec-4c75-8a73-293df3123aa9)
![image](https://github.com/user-attachments/assets/fab2e173-c9bf-45e6-a122-b8625d474e42)

Create an ADF pipeline
Add Copy Data activity for copying on premise data
![image](https://github.com/user-attachments/assets/a202f4a1-1305-4f0e-87d4-a6e8f833787b)
![image](https://github.com/user-attachments/assets/af4e4144-fb1c-4315-afdd-d5ff8f620c80)

10.	Launch Azure Databricks workspace and use it:
Create Databricks Clusters:
![image](https://github.com/user-attachments/assets/edfab1e1-963c-48a3-880b-621e26feedaa)

11.	Key Vault ( I won’t use key vault in this demo to run the ADF and Databricks, it is only for the information)
![image](https://github.com/user-attachments/assets/e23c9557-9d94-4190-a06e-c4abdca85983)

12.	ADLS Storage Creation For source data store (this will be our source for ETL)
![image](https://github.com/user-attachments/assets/2d373b63-dc72-4304-b61e-fcf20357e611)
![image](https://github.com/user-attachments/assets/9d640331-52d4-4365-a2e2-593c8b8fd674)
![image](https://github.com/user-attachments/assets/85166ae4-678d-4ba9-a537-d7c805cf84a5)

We will be processing Person Details in our ETL pipeline. Uploading person_raw.csv file.
![image](https://github.com/user-attachments/assets/c14e4d99-3f52-4d9d-8a5c-e11ea2de1af2)
 
13.	ADF Pipeline Creation.
a.	Linked Service Creation
Creating ADLS linked services to read and write data from source and target.
![image](https://github.com/user-attachments/assets/d1f13853-3bc8-4b66-b509-8277e24d760f)
![image](https://github.com/user-attachments/assets/b5f25399-f04c-4e24-8a41-a53599be365a)

Databricks Linked Service
![image](https://github.com/user-attachments/assets/78327243-4ba7-40ac-bb02-0ef825ce1999)
![image](https://github.com/user-attachments/assets/2c35f62e-4277-4c5a-a387-ab8818011e21)
![image](https://github.com/user-attachments/assets/667ec3ad-7c9b-448a-be6f-a1e803256c41)
![image](https://github.com/user-attachments/assets/e72c2fa8-4904-49c6-9f9c-f5f9db42a67a)
 
b.	Creating Data Pipelines and Datasets
copydata-bronze-pipeline creation (extracting person, email, phone and phone types details to bronze layer)
Update name of the pipeline in General tab.
![image](https://github.com/user-attachments/assets/84559a21-d8e2-4e05-86c4-427b5ce6ccca)

Update source details and include dataset with Parameters.
![image](https://github.com/user-attachments/assets/8a3c2513-3950-4ef0-814e-eac13d51ffb4)

Datasets
![image](https://github.com/user-attachments/assets/b09a4f23-66f2-4697-97e5-b72c54f65f7b)

Parameters under datasets (so we can reuse the same linked services). 
![image](https://github.com/user-attachments/assets/733dcdb0-33de-4891-ad2f-4a51487bbad7)

Same steps will be repeated for other three datasets.

Databricks Data pipeline
dbs_bronze_silver and dbs_silver_gold pipelines will be created, once we will write those notebooks in Databricks Workspace.
![image](https://github.com/user-attachments/assets/e9175a02-7e59-49bb-8d15-2031c422bec5)

Before writing notebooks, we need to create Databricks Clusters.

14.	Interactive Cluster creation for ADF data pipeline (can use job cluster as well).
![image](https://github.com/user-attachments/assets/60534dd9-3d08-4551-be73-06427eb2540a)

For setting the mount-point – we will check the credential pass through option. If you will uncheck credential pass through, then we should be able to use default Unity Catalog.
![image](https://github.com/user-attachments/assets/f1f1506d-e0bc-49a8-995e-096eae405cfd)

15.	Setup a mount points to read data from ADLS paths
![image](https://github.com/user-attachments/assets/8fcd6d22-0268-4abe-97ac-a84f27c0bfe9)

16.	Create notebooks to transform bronze data to silver to gold.
![image](https://github.com/user-attachments/assets/5147207a-c2a1-4555-a824-c9b94f2389ca)
![image](https://github.com/user-attachments/assets/9c18688d-bb84-4e52-9f37-30204824946e)

17.	First, we will attach the Azure Databricks Linked Service that we created with Interactive Cluster
![image](https://github.com/user-attachments/assets/a0e5e26b-f6c8-406d-9635-b9f56ce5c963)
![image](https://github.com/user-attachments/assets/880e4410-8bbe-40f0-8e06-2b1d62eb42e7)
18.	Now you can attach those notebooks to ADF pipelines.
![image](https://github.com/user-attachments/assets/12d1e7b9-39df-44b5-ae00-7a450b0acc18)

19.	Now will create a parent Pipeline to run those child pipeline in sequence.
![image](https://github.com/user-attachments/assets/d9827a5b-71da-417d-99bf-97e8f313fcc6)
![image](https://github.com/user-attachments/assets/cb7005e2-b09f-4af2-b2b6-357488f3f98c)

20.	Trigger pipeline from ADF or manually debug.
![image](https://github.com/user-attachments/assets/6a3cd535-3ff1-487e-b738-db76bdfcebb1)
![image](https://github.com/user-attachments/assets/0725982a-d66f-4746-9f23-ae77a6b9696c)

21.	If you would like to skip ADF and only wants to use Databricks. We can use Databricks workflow for orchestration and scheduling.
![image](https://github.com/user-attachments/assets/c1e24e1a-637f-4856-aa9e-36feaf90f7c3)

It is preferred to use job-clusters. I am using interactive for this demo.
![image](https://github.com/user-attachments/assets/ca858f30-6f7d-4c50-9b2f-b358249c5c92)
![image](https://github.com/user-attachments/assets/63644082-c0d1-4202-92ef-6cb0bfcb31c7)


We can click on run-now to run the job and set trigger for scheduling.
 
 

 

 

 
 


22.	Integrate with Power BI and build a sample report.
Navigate to Catalog - > Hive Metastore - > Click on Open in Power BI Desktop
 
 
Save *.pbids file on your desktop

 

There are three different options to connect
 

I will be using personal access token for easy access. We can use Entra-ID to connect. Or you can load the data to Synapse Analytics, SQL Server Managed Instance for presentation layer.

 
 
Generating Personal Access Token for Power BI.

 
Now we can use this token to connect to PBI.

 

Now you could see those hive metastore tables from Power BI
 
 
We can use Power BI - > Get Data - > Type Databricks - > then connect to Azure Databricks. There are different ways to connect.

 

Sample Power BI Report
 
