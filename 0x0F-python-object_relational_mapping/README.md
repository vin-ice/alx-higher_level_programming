# Python - Object-relational mapping
## Context
- In this project, you will link two amazing worlds: Databases and Python!
- In the first part, you will use the module  `MySQLdb` to connect to a MySQL database and execute your SQL queries.
- In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).  
## Resources
- [Object-relational mappers](https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A)
- [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw)
- [MySQLdb tutorial](https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA)
- [SQLAlchemy tutorial](https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA)
- [SQLAlchemy](https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA)
- [mysqlclient/MySQLdb](https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q)
- [Introduction to SQLAlchemy](https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA)
- [Flask SQLAlchemy](https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg)
- [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg)
- [Python SQLAlchemy Cheatsheet](https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q)
- [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of - - SQLAlchemy is the same with MySQL)](https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ)
- [SQLAlchemy Tutorial](https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ)  
## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.5)
- Your files will be executed with `MySQLdb` version 2.0.x
- Your files will be executed with `SQLAlchemy` version 1.4.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy  
## Installation
### MYSQLdb  
`sudo apt-get install python3-dev`  
`sudo apt-get install libmysqlclient-dev`  
`sudo apt-get install zlib1g-dev`  
`sudo apt-get install mysqlclient`  
...  
`$ python3`  
`>>> import MySQLdb`  
`>>> MySQLdb.version_info`   
(2, 0, 3, 'final', 0)  
### SQLAlchemy  
`$ sudo pip3 install SQLAlchemy`  
...  
`$ python3`  
`>>> import sqlalchemy`  
`>>> sqlalchemy.__version__`   
'1.4.22'