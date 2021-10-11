# Start
Schema -> Table -> Row/Column (Record/Field)  
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci  
`utf8mb4` : U+FFFF 이후 unicode를 지원해줌. 원래는 `utf8mb3`가 기본이고 이는 Basic Multilingual Plane만 지원  
`0900` : Unicode의 collation algorithm 9.0.0 지원  
`ai` : accent insensitivity  
`ci` : case insensitivity  

MySQL 변경을 위해서는 무조건 root 계정에 접속해야함.  
계정은 `mysql` 데이터베이스의 `user` table에서 관리
```bash
pip install mysql-connector
pip install mysql-connector-python
```

```sql
\connect root@localhost:3306
SELECT Host, User, account_locked, password_expired FROM mysql.user;
SELECT user() /* current user */
SELECT user, host, db, command FROM information_schema.processlist; /* current logged user */

```
## (1) Reset password
```bash
# C:\Program Files\MySQL\MySQL Server 8.0\bin
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

## sys
MySQL 서버의 성능 관련 정보들을 갖고있는 DB
```sql
SELECT * FROM sys.sys_config;
```
