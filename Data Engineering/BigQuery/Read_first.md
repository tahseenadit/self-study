Your query performance depends on two things:
- How you materialized (physically store data)  your table (like partioning, clustering etc).
- How you are reading and processing (joining for example) your data.

These two things affect the required resource allocations: Compute, Memory, I/O
