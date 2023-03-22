# Databricks notebook source
# DBTITLE 1,Comando 1 fodase
print("Olá mundo!!!")

# COMMAND ----------

# DBTITLE 1,Soma idiota
print("Isso é uma soma de 2+2 =",2+2)

# COMMAND ----------

# DBTITLE 1,Display dados
df = spark.table("silver.olist.pedido")
df.display()
