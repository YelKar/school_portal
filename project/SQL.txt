# Создание базы данных
  CREATE DATABASE <db name>;
# Удаление
  DROP DATABASE <db name>;

# Создание/удаление таблицы
  CREATE TABLE <table>(
    <column name1> <data type>,              # types: INT, VARCHAR(max_size), CHAR(size), DATE
    <column name2> <data type> NOT NULL AUTO_INCREMENT,
    <column name3> <data type>,
    PRIMARY KEY(<culumn name>)              # Первичный столбец
  );
  
  DROP TABLE <table>;

# Добавление данных
  INSERT INTO 
    <table> 
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
    );

# Обновление данных
  UPDATE <table> SET <column> = <value> WHERE <bool>;

# bool 1/0
  "=", "<", ">", "<=", ">=", "!=" / "<>"        # id = 5
  AND, OR, NOT                                  # id = 5 OR id > 100
  IS                                            # name IS NULL
  BETWEEN <from> AND <to>                       # id BETWEEN 5 AND 10     =>    id => 5 AND id <= 10
  IN(<value1>, <value2>, <value3>)              # id IN(2, 5, 7)          =>    id = 2 OR id = 5 OR id = 7
  LIKE "%...%"/"%..."/"...%"                    # name LIKE "%a%"         =>    < if "a" in name  =>  1 >
  
