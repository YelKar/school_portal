# Flask_wtf

## create form
### import FlaskForm, Fields and validators

```python
from flask_wtf import FlaskForm
from wtforms import FieldType
from wtforms.validators import SomeValidator
```

### Create class
```python
class MyForm(FlaskForm):
    field_name = FieldType("label text", 
                           validators=[SomeValidator()]
                           render_kw={
                               "field-tag-argument": "value", 
                               "argument2": "value2"
                               }
                           )
```

## view form
### Flask backend
```python
@app.route("/form", methods=["GET", "POST"])     # routegp + TAB
def form_view():
    form = MyForm()
    if form.validate_on_submit():    # check validate
        print(form.field_name.data)     # get and print entered data
    return render_template("form.html", form=form)
```

### frontend. Template

#### not use "for"
```html
<form method="POST">
    {{ form.csrf_token }}
    <p>
        {% if form.field_name.errors %}
            <div>
                {% for error in form.field_name.errors %}
                    {{ error if error }}
                {% endfor %}
            </div>
        {% endif %}
        {{ form.field_name }}
        {{ form.field_name.label() }}
    </p>
</form>
```

#### with "for"
```html
<form method="POST">
    {{ form.csrf_token }}
    {% for field in form if field.name != "csrf_token" %}
        <p>
            {% if field.errors %}
                <div class="form_error">
                    {% for error in field.errors %}
                        {{ error if error }}
                    {% endfor %}
                </div>
            {% endif %}
            {{ field.label() if field.type != "SubmitField" }}<br>
            {{ field }}
        </p>
    {% endfor %}
</form>
```

## Field types
```StringField``` - ```<input type="text">```
| Таблицы       | Это                | Круто |
| ------------- |:------------------:| -----:|
| столбец 3     | выровнен вправо    | $1600 |
| столбец 2     | выровнен по центру |   $12 |
| зебра-строки  | прикольные         |    $1 |
