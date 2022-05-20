"""Creating filters for jinja"""

from application import application
import datetime


@application.template_filter("fromTimestamp")
def from_timestamp_filter(product) -> datetime.datetime:
    """

    :param product:
    :return: datetime.datetime
    """
    return datetime.datetime.fromtimestamp(product)


@application.template_filter("strftime")
def strftime_filter(product: datetime.datetime, form: str) -> str:
    """

    :param product:
    :param form:
    :return:
    """
    return product.strftime(form)


@application.template_filter("line_breaks")
def line_breaks(product: str):
    """

    :param product:
    :return:
    """
    return product.replace("\n", "<br>")
