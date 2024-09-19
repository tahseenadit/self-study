Your query performance depends on two things:
- How you materialized (physically store data)  your table (like partioning, clustering etc).
- How you are reading and processing (joining for example) your data.

These two things affect the required resource allocations: Compute, Memory, I/O.

BigQuery is a disaggregated storage and compute engine.

### Where does bigquery store it's data ?

Usually the data in BigQuery is stored on Google's distributed file system - Colossus

### In which format bigquery stores it's data ?

Most often in blocks in Capacitor format

### What system is used by bigquery to process it's data ?

The compute is represented by Borg tasks.

Bigquery is dynamic, which means the query plan can be modified while a query is running. What does it mean ? It means it can improve data distribution throughout query workers. This is a feature of **Dremel** . 

### DDL and DML
DDL stands for Data Definition Language and refers to SQL commands used to create, modify, and delete database structures such as tables, indexes, and views. DML stands for Data Manipulation Language and refers to SQL commands used to insert, update, and delete data within a database.
