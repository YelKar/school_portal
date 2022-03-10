# Flask_SQLalchemy

### Create database object

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
```

### create table class
```python
class TableClass(db.Model):
    column_name = db.Column(db.datatype, attributes)
    
    def __repr__(self):
        return f"<table_name {self.column_name}>"
```
