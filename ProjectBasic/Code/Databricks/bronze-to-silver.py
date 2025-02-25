# Databricks notebook source
# MAGIC %md
# MAGIC ## Bronze To Silver Data Transformation For Person Details

# COMMAND ----------

from pyspark.sql.functions import lit, current_timestamp
from pyspark.sql.types import *

def bronzeToSilverDeltaTblUCWithDatabase(
    database_name: str, 
    table_name: str, 
    parquet_file_path: str, 
    location: str,
    column_schema: dict,
    source_to_target_mapping: dict = None
):
    """
    Create a Delta table in Unity Catalog with dynamic data type conversion and optional column renaming.
    
    Args:
    database_name (str): The name of the Unity Catalog database.
    table_name (str): The name of the table to be created.
    parquet_file_path (str): Path to the Parquet file in DBFS mount point.
    location (str): The location (path) in the Unity Catalog's storage for Delta table.
    column_schema (dict): Dictionary of target column names and their respective data types.
    source_to_target_mapping (dict, optional): Mapping of source column names to target column names (if renaming is needed).
    
    Returns:
    None
    """
    # Ensure the hive metastore database exists
    spark.sql(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    
    # Read Parquet file into DataFrame
    df = spark.read.parquet(parquet_file_path)
    
    # Optional: Rename columns based on source-to-target mapping
    if source_to_target_mapping:
        for source_col, target_col in source_to_target_mapping.items():
            df = df.withColumnRenamed(source_col, target_col)

    # Select and cast columns based on the target schema
    for col_name, col_type in column_schema.items():
        if col_name in df.columns:
            df = df.withColumn(col_name, df[col_name].cast(col_type))
        
    # Add metadata columns
    df = df.withColumn("File_Path", lit(parquet_file_path)).withColumn("Create_DT", current_timestamp())

    # Show the first few rows (optional, for verification)
    display(df.printSchema())
    
    # Define the full table path
    full_table_path = f"{database_name}.{table_name}"
    
    # Writing data to Delta table
    df.write.format("delta") \
            .mode("overwrite") \
            .option("mergeSchema", "true") \
            .option("path", location) \
            .saveAsTable(full_table_path)
    
    # Optional: Register the table explicitly
    databricks_sql = f"""
        CREATE TABLE IF NOT EXISTS {full_table_path} 
        USING DELTA
        LOCATION '{location}'
    """
    spark.sql(databricks_sql)
    print(f"Delta table '{table_name}' created in Unity Catalog at location: {location}")


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ##### Load Person Data
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import lit, current_timestamp

# Specify the DBFS path for the Parquet file
parquet_file_path = "/mnt/bronze/person/person"

# Specify your Unity Catalog database, table, and storage path
database_name = "person_db"
table_name = "person"
location = "/mnt/silver/person/person"

# Define schema as a dictionary
column_schema = {
    "BusinessEntityID": "int",
    "PersonType": "string",
    "NameStyle": "string",
    "Title": "string",
    "FirstName": "string",
    "MiddleName": "string",
    "LastName": "string",
    "Suffix": "string",
    "EmailPromotion": "int",  
    "rowguid": "string",
    "ModifiedDate": "timestamp"  
}

source_to_target_mapping = {
    "BusinessEntityID": "BusinessEntityID",
    "PersonType": "PersonType",
    "NameStyle": "NameStyle",
    "Title": "Title",
    "FirstName": "FirstName",
    "MiddleName": "MiddleName",
    "LastName": "LastName",
    "Suffix": "Suffix",
    "EmailPromotion": "EmailPromotion",
    "rowguid": "rowguid",
    "ModifiedDate": "ModifiedDate"
}

# Create the Delta table in hive metastore using the Parquet file
bronzeToSilverDeltaTblUCWithDatabase(
    database_name,
    table_name,
    parquet_file_path,
    location,
    column_schema,
    source_to_target_mapping
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ##### Load Email Data

# COMMAND ----------

# Specify the DBFS path for the Parquet file
parquet_file_path = "/mnt/bronze/person/email"

# Specify your Unity Catalog database, table, and storage path
database_name = "person_db"
table_name = "email"
location = "/mnt/silver/person/email"

# Define schema as a dictionary
column_schema = {
    "BusinessEntityID": "int",
    "EmailAddressID": "int",
    "EmailAddress": "string",
    "Rowguid": "string",
    "ModifiedDate": "timestamp"
}

source_to_target_mapping = {
    "BusinessEntityID": "BusinessEntityID",
    "EmailAddressID": "EmailAddressID",
    "EmailAddress": "EmailAddress",
    "Rowguid": "rowguid",
    "ModifiedDate": "ModifiedDate"
    }

# Create the Delta table in hive metastore using the Parquet file
bronzeToSilverDeltaTblUCWithDatabase(
    database_name,
    table_name,
    parquet_file_path,
    location,
    column_schema,
    source_to_target_mapping
)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Load Phone Data

# COMMAND ----------

# Specify the DBFS path for the Parquet file
parquet_file_path = "/mnt/bronze/person/phone"

# Specify your Unity Catalog database, table, and storage path
database_name = "person_db"
table_name = "phone"
location = "/mnt/silver/person/phone"

# Define schema as a dictionary
column_schema = {
    "BusinessEntityID": "int",
    "PhoneNumber": "string",
    "PhoneNumberTypeID": "int",
    "ModifiedDate": "timestamp"
}

source_to_target_mapping = {
    "BusinessEntityID": "BusinessEntityID",
    "PhoneNumber": "PhoneNumber",
    "PhoneNumberTypeID": "PhoneNumberTypeID",
    "ModifiedDate": "ModifiedDate"
    }

# Create the Delta table in hive metastore using the Parquet file
bronzeToSilverDeltaTblUCWithDatabase(
    database_name,
    table_name,
    parquet_file_path,
    location,
    column_schema,
    source_to_target_mapping
)

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS person_db.email1")
dbutils.fs.rm("/mnt/silver/person/email1", True)

# COMMAND ----------

# Specify the DBFS path for the Parquet file
parquet_file_path = "/mnt/bronze/person/phonenumbertype"

# Specify your Unity Catalog database, table, and storage path
database_name = "person_db"
table_name = "phonenumbertype"
location = "/mnt/silver/person/phonenumbertype"

# Specify the list of columns to select
columns = ["PhoneNumberTypeID", "Name", "ModifiedDate"]

# Define schema as a dictionary
column_schema = {
    "PhoneNumberTypeID": "int",
    "Name": "string",
    "ModifiedDate": "timestamp"
}

source_to_target_mapping = {
    "PhoneNumberTypeID": "PhoneNumberTypeID",
    "Name": "Name",
    "ModifiedDate": "ModifiedDate"
    }

# Create the Delta table in hive metastore using the Parquet file
bronzeToSilverDeltaTblUCWithDatabase(
    database_name,
    table_name,
    parquet_file_path,
    location,
    column_schema,
    source_to_target_mapping
)