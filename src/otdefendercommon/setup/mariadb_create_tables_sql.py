from sqlalchemy.schema import CreateTable
from sqlalchemy.dialects import mysql
from otdefendercommon.database.base import Base
import otdefendercommon.models  # Ensures all models are registered

def print_mariadb_ddl():
    for table in Base.metadata.sorted_tables:
        # Add DROP TABLE IF EXISTS as a comment before the create table statement
        print(f"-- DROP TABLE IF EXISTS `{table.name}`;")
        # Compile each table using the MySQL/MariaDB dialect
        sql = str(CreateTable(table).compile(dialect=mysql.dialect()))
        print(sql)
        print(";\n\n")  

if __name__ == "__main__":
    print_mariadb_ddl()