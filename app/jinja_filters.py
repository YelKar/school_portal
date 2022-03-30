from app import app
import datetime


@app.template_filter("fromTimestamp")
def from_timestamp_filter(product):
    return datetime.datetime.fromtimestamp(product)


@app.template_filter("strftime")
def strftime_filter(product: datetime.datetime, form: str):
    return product.strftime(form)
