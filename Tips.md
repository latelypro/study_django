# DjangoでPostgreSQLを使う

|name|version|
|--|--|
|macOS High Sierra| 10.13.4|
|Python|3.6.5|
|Django|2.1.3|
|PostgreSQL|11.1|
## postgreSQLのインストール

```Console:install command
brew install postgresql
```

```Console:version check
psql --version
psql (PostgreSQL) 11.1
```

## データベースバインディングのインストール

```Console:install command
pip install psycopg2
```

## DBの設定

### init db

```Console:init db
% initdb /usr/local/var/postgres -E utf8
The files belonging to this database system will be owned by user "duchida".
This user must also own the server process.

The database cluster will be initialized with locale "ja_JP.UTF-8".
initdb: could not find suitable text search configuration for locale "ja_JP.UTF-8"
The default text search configuration will be set to "simple".

Data page checksums are disabled.

initdb: directory "/usr/local/var/postgres" exists but is not empty
If you want to create a new database system, either remove or empty
the directory "/usr/local/var/postgres" or run initdb
with an argument other than "/usr/local/var/postgres".
```

### start server

```Consple:start server
% pg_ctl -D /usr/local/var/postgres start
waiting for server to start....2018-12-12 20:44:33.569 JST [33393] LOG:  listening on IPv6 address "::1", port 5432
2018-12-12 20:44:33.569 JST [33393] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2018-12-12 20:44:33.571 JST [33393] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5432"
2018-12-12 20:44:33.592 JST [33394] LOG:  database system was shut down at 2018-12-12 20:43:31 JST
2018-12-12 20:44:33.598 JST [33393] LOG:  database system is ready to accept connections
 done
server started
```

### DB list 取得

```Console:get db list
% psql -l
                                List of databases
   Name    |  Owner  | Encoding |   Collate   |    Ctype    |  Access privileges
-----------+---------+----------+-------------+-------------+---------------------
 postgres  | duchida | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | duchida | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/duchida         +
           |         |          |             |             | duchida=CTc/duchida
 template1 | duchida | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/duchida         +
           |         |          |             |             | duchida=CTc/duchida
(3 rows)
```

## DB置き場のパスを設定

```Console:.zprofile
export PGDATA=/usr/local/var/postgres
```

PGDATAを設定することで起動と終了のコマンドが簡単に。  

```Console: pg_ctl start
% pg_ctl start
waiting for server to start....2018-12-12 20:52:47.759 JST [33887] LOG:  listening on IPv6 address "::1", port 5432
2018-12-12 20:52:47.759 JST [33887] LOG:  listening on IPv4 address "127.0.0.1", port 5432
2018-12-12 20:52:47.761 JST [33887] LOG:  listening on Unix socket "/tmp/.s.PGSQL.5432"
2018-12-12 20:52:47.782 JST [33888] LOG:  database system was shut down at 2018-12-12 20:51:41 JST
2018-12-12 20:52:47.789 JST [33887] LOG:  database system is ready to accept connections
 done
server started
```

```Console: pg_ctl stop
% pg_ctl stop
waiting for server to shut down....2018-12-12 20:53:55.686 JST [33887] LOG:  received fast shutdown request
2018-12-12 20:53:55.687 JST [33887] LOG:  aborting any active transactions
2018-12-12 20:53:55.687 JST [33887] LOG:  background worker "logical replication launcher" (PID 33894) exited with exit code 1
2018-12-12 20:53:55.688 JST [33889] LOG:  shutting down
2018-12-12 20:53:55.704 JST [33887] LOG:  database system is shut down
 done
server stopped
```

## ユーザーの追加と確認

### ユーザー作成

```Console:create user
% createuser -P [user_name]
Enter password for new role:
Enter it again:
```

### ユーザーの確認

```Console: User List
% psql -q -c'select * from pg_user' [db name]
    usename    | usesysid | usecreatedb | usesuper | userepl | usebypassrls |  passwd  | valuntil | useconfig
---------------+----------+-------------+----------+---------+--------------+----------+----------+-----------
 duchida       |       10 | t           | t        | t       | t            | ******** |          |
 djangodb_user |    16384 | f           | f        | f       | f            | ******** |          |
(2 rows)
```

## DB作成

```Console:createdb command
% createdb [dbname] -O [owner_user_name]
```

## できてるか確認

```Console: createdb exsample
% createdb django-db -O djangodb_user
% psql -l
                                   List of databases
   Name    |     Owner     | Encoding |   Collate   |    Ctype    |  Access privileges
-----------+---------------+----------+-------------+-------------+---------------------
 django-db | djangodb_user | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 postgres  | duchida       | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | duchida       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/duchida         +
           |               |          |             |             | duchida=CTc/duchida
 template1 | duchida       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/duchida         +
           |               |          |             |             | duchida=CTc/duchida
```

## DB接続

```Console: connect command
% psql -U [login_user_name] [db_name]
```

```Console: connect example
% psql -U djangodb_user django-db
psql (11.1)
Type "help" for help.

django-db=>
```

## Django側の設定

```JSON:settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DBNAME',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

```Console:migrate
python manage.py makemigrations
python manage.py migrate
```

## Twitter風ページを作る

参考：[PHP を使って Twitter 風のシステムをサイトに構築する](https://www.ibm.com/developerworks/jp/opensource/library/os-php-twitter-interface/index.html)