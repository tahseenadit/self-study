# Query Execution
- JOIN stage that generates far more output rows than input rows can indicate an opportunity to filter earlier in the query.
-  If you observe that the number of active units remains limited throughout the lifetime of the query but the amount of queued units of work remains high, this can represent cases where reducing the number of concurrent queries can significantly improve overall execution time for certain queries.
    Let's see an example:
    
    #### Scenario 1: Executing 3 Units Simultaneously
    - You have **12 slots** (resources) available.
    - Each unit (query) requires **6 slots** to run efficiently.
    - If you run **3 units (queries)** simultaneously:
      - 3 units × 6 slots per unit = **18 slots needed**.
      - But you only have **12 slots available**.
      - This means there is a shortage of slots, so some of the units will need to **wait for slots to free up**. This results in resource contention and possibly longer execution times for the queries because they are not receiving enough resources to run efficiently.
    
    #### Scenario 2: Executing 2 Units Simultaneously
    - You still have **12 slots** available.
    - Each unit still requires **6 slots**.
    - If you run **2 units (queries)** simultaneously:
      - 2 units × 6 slots per unit = **12 slots needed**.
      - You have exactly **12 slots available**.
      - This means both units will be allocated the required slots immediately, and they can run at full efficiency without any waiting or queuing.

    By reducing the number of simultaneous units from 3 to 2, you can ensure that each unit gets the full number of slots it requires (6 slots each), avoiding any waiting or queuing. This results in **faster and more efficient execution** for those queries.

# Federated Query
- A federated query is likely to not be as fast as querying only BigQuery storage. Also, the source database might not be optimized for complex analytical queries.
- You must create the connection resource in the same project as the Cloud SQL or AlloyDB instance.
- If your external query contains a data type that is unsupported in BigQuery, the query fails immediately. You can cast the unsupported data type to a different supported data type.
- The external query that is executed in the source database must be read-only. Therefore, DML or DDL statements are not supported.
