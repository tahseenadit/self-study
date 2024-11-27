Suppose there is a .csv file. Will you upload it in cloud storage or create a table for it in bigquery ?

# Workload Requirements
**Does the user download the file as a whole in his editor like databricks notebook?**

If so, then the user probably downloads other data and create dataframes and then perform operations.

**Does the user directly query the data using sql?**

If so, then probably the user won't access the csv fle as a whole but would be interested to have the data from the csv file as a table that can be queried directly using sql.

# Permission requirements
**Does the user need file-level access control?**
**What is the access granularity that you need to implement?**

# Performance requirements
- Frequent read and write
- Frequent read and less write
- Less read and frequent write
- less read and less write

While answering the above questions, consider the volume of the data.
- Buffer or queuing technology of the cloud storage or bigquery
- Caching mechanism
- Retention policy
- Throughput bandwidth
- Scaling
- Handling parallel requests

# Cost requirements
- Infra cost
- Network cost
