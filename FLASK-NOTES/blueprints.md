### blueprint
- We use blueprints so we can register multiple sub-applications to main application

```from flask import Blueprint```

### Lets assume you've a project structure

```text

project_dir  (project root)   (aka main application)

    - IDAM  (sub-application1)
        - __init__.py
        - auth.py 
        
    - saving_account  (sub-application2)
        - __init__.py
        - saving.py
        
    - requirements.txt (dependency)
    - main.py (entrypoint) [application instatiation will always be in entrypoint]
    
```


### banks

```
IDAM (Identity And Access Management)
    <home-url>/idamapi/authenticate   (HTTP GET / POST)
    <home-url>/idamapi/authorize      (HTTP GET / POST)

saving_account
    <home-url>/savingapi/saving/deposit    (HTTP GET / POST)
    <home-url>/savingapi/saving/withdrawl   (HTTP GET / POST)
    
```


# SQL query for update

```sql
# syntax
update <table-name> set column1="value1", column2="value2" where primary_key=<primary_value>;

# actual query
update starwarsDB.characters set name='prashant', height='1.74' where char_id=73;
```

# SQL QUERY FOR `UPSERT`


#### UPSERT = INSERT + UPDATE

```sql

# syntax
INSERT INTO <TABLE_NAME> (column1, column2) VALUES (value1, valu2) ON DUPLICATE KEY UPDATE column1=<value1>, column2=<value2>


select * from starwarsDB.characters;
insert into starwarsDB.characters (char_id, name) values (74, "rahul") ON DUPLICATE KEY UPDATE name="rahul";
```