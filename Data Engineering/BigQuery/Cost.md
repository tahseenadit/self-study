### Bigquery charges for the bytes processed
You need to understand what it means. You actually pay for the volume of data loaded in the workers. Of course, you do nothing in your request and you ask for the 20 first result, the query stop earlier, and all the data aren't processed, but at least loaded. And you will pay for this!

### What happens if you use `limit` in your query ?

Example: select * from some_table limit 100

Bigquery still loads the full table, then processes 100 rows. Because you actually pay for the volume of data loaded in the workers, you are actually charged for the full table, not for the 100 rows. 

Take another example where your full table size is 794 GB and the table has 244928379 rows and you want to read only 163514 rows. In Execution details it can be stated that only 0.067 % of rows (244928379/163514) were read. That is not a full table scan. But you may see 794 GB which is the full table size. Actually you are charged for (loading) 244928379 rows but you only read (process) 0.067%. 
You can achieve very complex formula and filtering, joining (...) on the same amount of data, for the same cost. Therefore, use BigQuery to transform and deep dive into your data, not to perform usual 'MySQL' query.

Now there are optimizations done by bigquery which can affect the cost. `limit 100` gives a lot of possibilities. Like taken the last 100 entries from cache (which could be cached because of current timing of write or read or because it's often used. Goal is to minimize reads/cost and maximize performance. So, if it is already in the cache, then bigquery does not need to load the full table. Which may reduce the amount billed. The word `cache` has more information related to it. Like cache of what ? Cache memory of different worker nodes. Workers will unload the contents if data hasn't been used for over 24 hours.

So you have to think differently when you work with BigQuery, it's analytics database and not designed to perform small requests (too slow to start, the latency is at least 500ms due to worker warm up).And you pay for the reservation and the load cost (moving data have a cost and reserving slots has also a cost). The query results are stored in a temporary table. You can see that in the 'Destination Table' field under the 'Job Information' tab. You are also charged for that.

Somewhere it is stated that as of december 2021, select * from Limit, will not scan the whole table and you pay only for a small number of rows, obviously if you add `order by`, it will scan everything because then it has to scan the full table to find the right order even if you read only few rows from your table. But that is not the actual case as far as I have experienced. Bigquery still processes (loads) the full table even if you use `limit` as of September 2024.

### What can you do to minimize cost ?

- Use specific columns instead of selecting all columns with (*). Because bigquery is a columnar storage, if you just select the columns you need, then you reduce the amount of data bigquery will load.
- You can use Table Sampling which prevents BQ to do a full table scan. eg:- SELECT * FROM dataset.my_table TABLESAMPLE SYSTEM (50 PERCENT) WHERE customer_id = 1
- Table Partitioning Big query can partition data using either a Date/Datetime/Timemestamp column you provide or by insert date (which is good if you have regular updates on a table). In order to do this, you must specify the partition strategy in the DDL:

  ```
  CREATE TABLE mydataset.mytable (foo: int64, txdate:date)
  PARTITION BY txdate
  ```

- **Wildcard tables (like Sharding - splitting the data into multiple tables)**: This works when your data holds information about different domains (geographical, customer type, etc.) or sources. Instead of having one big table, you can create 'subtables' or 'shards' like this with a similar schema (usually people use the same). For instance, `dateset.tablename.eur` for european data and `dataset.tablename.jap` for data from Japan. You can query one of those tables directly select col1,col2... from dataset.tablename.custromer_eur;  or from all tables select col1,col2 from 'dataset.tablename.*'.  Wildcard tables can be also partitioned by date.
