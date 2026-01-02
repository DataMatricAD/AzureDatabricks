# Databricks notebook source
# MAGIC %md
# MAGIC ##  Silver to Gold Data Transformation For Person Details

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS person_db.person_gold
# MAGIC USING delta
# MAGIC LOCATION '/mnt/gold/person/'
# MAGIC AS
# MAGIC SELECT 
# MAGIC     per.BusinessEntityID,
# MAGIC     per.PersonType,
# MAGIC     per.Title,
# MAGIC     per.FirstName,
# MAGIC     per.MiddleName,
# MAGIC     per.LastName,
# MAGIC     eml.EmailAddress,
# MAGIC     per.EmailPromotion,
# MAGIC     phe.PhoneNumber
# MAGIC FROM person_db.person per
# MAGIC JOIN person_db.email eml
# MAGIC ON per.BusinessEntityID = eml.BusinessEntityID
# MAGIC JOIN person_db.phone phe
# MAGIC ON per.BusinessEntityID = phe.BusinessEntityID;
# MAGIC
# MAGIC MERGE INTO person_db.person_gold tgt
# MAGIC USING (
# MAGIC   SELECT 
# MAGIC       per.BusinessEntityID,
# MAGIC       per.PersonType,
# MAGIC       per.Title,
# MAGIC       per.FirstName,
# MAGIC       per.MiddleName,
# MAGIC       per.LastName,
# MAGIC       eml.EmailAddress,
# MAGIC       per.EmailPromotion,
# MAGIC       phe.PhoneNumber
# MAGIC   FROM person_db.person per
# MAGIC   JOIN person_db.email eml
# MAGIC   ON per.BusinessEntityID = eml.BusinessEntityID
# MAGIC   JOIN person_db.phone phe
# MAGIC   ON per.BusinessEntityID = phe.BusinessEntityID
# MAGIC ) src
# MAGIC ON tgt.BusinessEntityID = src.BusinessEntityID
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET
# MAGIC     tgt.PersonType = src.PersonType,
# MAGIC     tgt.Title = src.Title,
# MAGIC     tgt.FirstName = src.FirstName,
# MAGIC     tgt.MiddleName = src.MiddleName,
# MAGIC     tgt.LastName = src.LastName,
# MAGIC     tgt.EmailAddress = src.EmailAddress,
# MAGIC     tgt.EmailPromotion = src.EmailPromotion,
# MAGIC     tgt.PhoneNumber = src.PhoneNumber
# MAGIC WHEN NOT MATCHED THEN
# MAGIC   INSERT (
# MAGIC     BusinessEntityID,
# MAGIC     PersonType,
# MAGIC     Title,
# MAGIC     FirstName,
# MAGIC     MiddleName,
# MAGIC     LastName,
# MAGIC     EmailAddress,
# MAGIC     EmailPromotion,
# MAGIC     PhoneNumber
# MAGIC   ) VALUES (
# MAGIC     src.BusinessEntityID,
# MAGIC     src.PersonType,
# MAGIC     src.Title,
# MAGIC     src.FirstName,
# MAGIC     src.MiddleName,
# MAGIC     src.LastName,
# MAGIC     src.EmailAddress,
# MAGIC     src.EmailPromotion,
# MAGIC     src.PhoneNumber
# MAGIC   );