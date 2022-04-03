"""Creating filters for jinja"""

from app import app
import datetime


@app.template_filter("fromTimestamp")
def from_timestamp_filter(product) -> datetime.datetime:
    """

    :param product:
    :return: datetime.datetime
    """
    return datetime.datetime.fromtimestamp(product)


@app.template_filter("strftime")
def strftime_filter(product: datetime.datetime, form: str) -> str:
    """

    :param product:
    :param form:
    :return:
    """
    return product.strftime(form)
