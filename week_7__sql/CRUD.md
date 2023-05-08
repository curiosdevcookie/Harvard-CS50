# SQL Database

## CRUD

### Create (create, insert)

```sql
CREATE TABLE IF NOT EXISTS table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

```sql
CREATE INDEX ON table_name (column1, column2, column3) # creates a b-tree
```

### Read (select)

```sql
SELECT column1, column2, ...
FROM table_name;
```

### Update (update)

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

### Delete (delete, drop)

```sql
DELETE FROM table_name
WHERE condition;
```

```sql
DROP TABLE table_name;
```

## SQL Functions

### COUNT

```sql
SELECT COUNT(column_name) FROM table_name;
```

```sql
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

### SUM

```sql
SELECT SUM(column_name) FROM table_name;
```

## SQL Praedicates

### LIKE

```sql
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;
```

### IN

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

### BETWEEN

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

### ALIAS

```sql
SELECT column_name AS alias_name
FROM table_name;
```

### JOIN

```sql
SELECT column_name(s)
FROM table_name1
INNER JOIN table_name2
ON table_name1.column_name = table_name2.column_name;
```

```sql
SELECT column_name(s)
FROM table_name1
LEFT JOIN table_name2
ON table_name1.column_name = table_name2.column_name;
```

```sql
SELECT column_name(s)
FROM table_name1
RIGHT JOIN table_name2
ON table_name1.column_name = table_name2.column_name;
```

```sql
SELECT column_name(s)
FROM table_name1
FULL JOIN table_name2
ON table_name1.column_name = table_name2.column_name;
```

### UNION

```sql
SELECT column_name(s) FROM table_name1
UNION ALL 
SELECT column_name(s) FROM table_name2;
```

### GROUP BY

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
```

### HAVING

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s) // show me once
HAVING condition
```

### EXISTS

```sql
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```

## Data Types in SQLITE

- BLOB (Binary large object)
- REAL (Float)
- INTEGER (Integer)
- TEXT (String)
- NUMERIC (dates and time)

## Constraints

- NOT NULL
- UNIQUE
- PRIMARY KEY (database will use that as the primary identifier)
- FOREIGN KEY (database will reference the primary key column in another table)
- CHECK (check if the value in a column meets a specific condition)
- DEFAULT (set a default value for a column if no value is specified)

