Parquet files are immutable, so you can't modify the file to update the column name. If you want to change the column name, read it into a DataFrame, change the name, and then rewrite the entire file. Renaming a column can be an expensive computation.

When you add data to a Parquet file, **the existing Parquet file is not modified directly**. Instead, a **new Parquet file** is created, and the old file remains untouched. Here's how it typically works:

### 1. **Immutability of Parquet Files**:
   - Parquet files are **immutable**, meaning once they are written, they cannot be modified or updated in place.
   - This is due to how Parquet is designed as a columnar storage format optimized for read performance. Direct modifications would break its internal structure, such as metadata, column statistics, and file alignment.
   - Therefore, when data needs to be appended or updated, a new file is created instead of modifying the existing file.

### 2. **Appending Data**:
   - When you append new data, a new Parquet file is written that contains the additional records.
   - The new data is **not merged** with the old Parquet file. Instead, the system simply adds a new Parquet file with the appended data to the storage (e.g., a new file in the same directory or folder in a data lake).

### 3. **File Management**:
   - Over time, if appending happens frequently, you may end up with many Parquet files in your storage, where each file contains a subset of the full dataset (e.g., partitioned by time or batch).
   - It’s common to perform a **compaction** operation periodically, which merges several small Parquet files into larger ones to optimize for read performance. However, this still involves writing new Parquet files and does not alter the original ones.

### 4. **Updating/Deleting Data**:
   - Similar to appending, when you need to update or delete data in a Parquet file, the original file is **not updated directly**.
   - Instead, the system creates new Parquet files that reflect the updated or deleted records, and then the metadata (or index) is updated to point to the new files. The old Parquet files may be marked as obsolete or eventually deleted.

### 5. **Delta Lake and Transactional Systems**:
   - Systems like **Delta Lake** or **Apache Hudi** handle these changes by using a **transaction log**. They maintain the immutability of Parquet files by keeping track of which files are currently valid and which have been superseded by new files.
   - When you append, update, or delete records in Delta Lake, it creates new Parquet files reflecting the changes and updates the transaction log to mark old files as obsolete.
   - The old files are not immediately deleted, but they may eventually be cleaned up by **garbage collection** processes.

### Example Workflow:
- You have a Parquet file with records from January.
- If you add new records for February, instead of appending them to the January Parquet file:
  - A new Parquet file is created for February's data.
  - Both files coexist in storage.
  - The system (e.g., Delta Lake or the file index) manages which files to read for a full dataset view.

In summary, when data is added to a Parquet-based system, **new files are created** rather than modifying the existing Parquet files. These files remain immutable, and systems like Delta Lake manage them by using metadata and transaction logs, eventually cleaning up old files if necessary.
