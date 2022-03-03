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
                           validators=[SomeValidator()],
                           render_kw={
                               "field-tag-argument": "value", 
                               "argument2": "value2"
                               }
                           )
```
<br>

---
<div style="border: 2px solid red; 
    border-radius: 5px; 
    background-color: rgba(255, 0, 0, 0.2);">

<h3 style="color: black; background-color: rgba(255, 0, 0, 0.5); margin: 0;">
if you need to validate email, you need to install it
</h3>

```
pip install email_validator
```
</div>

---

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
<table class="user_info">
    <tr>
        <th>Wtf field</th>
        <th>input type</th>
    </tr>
    <tr>
        <td>StringField</td>
        <td>text</td>
    </tr>
    <tr>
        <td>PasswordField</td>
        <td>password</td>
    </tr>
    <tr>
        <td>EmailField</td>
        <td>email</td>
    </tr>
    <tr>
        <td>BooleanField</td>
        <td>checkbox</td>
    </tr>
    <tr>
        <td>SubmitField</td>
        <td>submit</td>
    </tr>
</table>

## validators

```DataRequired()``` - checking if value exist

```Length(max=..., min=...)```

```EqualTo("field_name", "message")``` - checking for a match with another field

