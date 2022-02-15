# Создание базы данных
  CREATE DATABASE <db name>;
# Удаление
  DROP DATABASE <db name>;

# Создание/удаление таблицы
  CREATE TABLE <table name>(
    <column name> <data type>,              # types: INT, VARCHAR(max_size), CHAR(size), DATE
    <column name> <data type> NOT NULL / AUTO_INCREMENT
  );
  
  DROP TABLE <table name>
# Добавление данных
  INSERT INTO 
    <table name> 
    (
      <column name1>,
      <column name2>,
      <column name3>
    )
    VALUES 
    (
      <data1>,
      <data2>,
      <data3>
    )

