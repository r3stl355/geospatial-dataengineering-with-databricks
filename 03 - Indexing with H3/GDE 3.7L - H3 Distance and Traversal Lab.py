# Databricks notebook source
# MAGIC %md
# MAGIC # H3 Distance and Traversal Lab
# MAGIC 
# MAGIC This notebook presents some challanges to review your understanding of the H3 traversal and distance functions. This is done using a fictional use case where gas stations are compared.
# MAGIC 
# MAGIC ## Learning Goals
# MAGIC - Work with H3 traversal functions
# MAGIC - Work with H3 distance functions

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup
# MAGIC Run the following cell to setup mosaic and h3 functions

# COMMAND ----------

# MAGIC %run ../Includes/Setup-3

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Find the Best Gas Station Lab
# MAGIC 
# MAGIC Envision the following, you arrive home after a long day of work. You happen to live -very conveniently- at **0 degrees longitude, 0 degrees latitude**. Upon reaching the driveway you look at the gas meter and see that you only have **4L of gas left**. With the current gas prices it is worth it to look for the best deal you can get. Since your car uses **1L of gas for every 50 resolution 9 H3 cell**, you will not be able to reach all of the gas stations as you'll be out of gas before arriving there. You browse the internet and make note of the positions and liter prices of nearby gas stations. Sadly, now every gas station uses the same format for their location. Some use latitude and longitude, some use string representations of H3 cells and some use bigint representations of h3 cells. You have found the following
# MAGIC 
# MAGIC | Brand | Location | Price per Litre |
# MAGIC | --- | --- | --- |
# MAGIC | BP | (-0.090005621 0.005748641) | 2.21 |
# MAGIC | Chevron | (619056576374505471) | 2.05 |
# MAGIC | Exxon | (637070976607846463) | 1.94 |
# MAGIC | Gulf | (8d754e09804003f) | 1.89 |
# MAGIC | Mobil | (0.129706366 0.431238479) | 1.88 |
# MAGIC | Shell | (619056840577908735) | 1.71 |
# MAGIC | Texaco | (8d754ebaa94003f) | 1.42 |
# MAGIC 
# MAGIC Our cars gas tank holds **60L in total**. Once we completed the fueling trip, we want to get home with at least **55L in the tank**. Let's use our knowledge of H3 to spend the least amount of money during the trip!

# COMMAND ----------

# MAGIC %md 
# MAGIC First things first! Let's first cleanup this data. Create a dataframe with the following schema
# MAGIC 
# MAGIC | name | datatype | description |
# MAGIC | --- | --- | --- | 
# MAGIC | brand | STRING | Brand name of the gas station |
# MAGIC | gas_cell_id | BIGINT | H3 cell id of gas station in resolution 9 |
# MAGIC | price | DOUBLE | Price of gas in euros per litre |
# MAGIC 
# MAGIC HINT: use the `h3_resolution` function

# COMMAND ----------

# TODO
df_gas_station = sprak.createDataFrame(..., "brand STRING, gas_cell_id LONG, price DOUBLE")
df_home = spark.createDataFrame([(619056821840379903,)], "home_cell_id LONG")

# COMMAND ----------

# MAGIC %md
# MAGIC Use the `mosaic_kepler` magic to visualise the locations of the gas stations cell id and your home location on the map

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md
# MAGIC Now that we have an idea of the locations of the gas stations, let's see which gas stations we can reach from our home. Use the `h3_kring` function to find all the cells that can be reached from your home and join this with the gas station dataframe.

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md
# MAGIC If we pick the cheapest gas station we can reach and get a full tank of fuel. How much will we have spent and with how much gas do we reach our home? Is this the best we can do?

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md 
# MAGIC We could also do a two stop trip, getting a bit of expensive fuel to reach a previously out-of-range gas station. What is the best we can do using this strategy? 

# COMMAND ----------

# TODO
