# Start
MySQL 변경을 위해서는 무조건 root 계정에 접속해야함.  
계정은 mysql 데이터베이스의 user table에서 관리
```bash
pip install mysql-connector
pip install mysql-connector-python
```

```sql
\connect root@localhost:3306
SELECT host, user, account, password_expired FROM mysql.user;
SELECT user() /* current user */
SELECT user, host, db, command FROM information_schema.processlist; /* current logged user */

```
## (1) Reset password
```bash
mysqld --defaults-file="C:\\ProgramData\\MySQL\\MySQL Server 8.0\\my.ini" --init-file=D:\\mysql-init.txt # as administrator
```
```sql
# mysql-init.txt
ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
```
# Create new user
```sql
CREATE USER 'test'@'localhost' IDENTIFIED BY 'newpassword';
GRANT ALL PRIVILEGES ON `mytestdb` . * TO 'test'@'localhost';
/* DB 접근권한 부여 <Database> . <table> */
/* or */
GRANT ALL PRIVILEGES ON * . * TO 'test'@'localhost';
FLUSH PRIVILEGES;

DROP USER 'test'@'localhost';  /* Delete user */
```

# Interactions
```sql
CREATE DATABASE mytestdb;
SHOW DATABASES;
use <database_name> /* select target database */
SHOW TABLES
desc <table_name>  /* Show table structure */
CREATE TABLE test (blob_col BLOB, INDEX(blob_col(10)));
```
