import nvdlib
from datetime import date, timedelta, datetime
from calendar import THURSDAY


def get_thursdays() -> list:
    """
    Returns the dates of last thursday and this thursday
    :return: list of strings
    """
    today = date.today()
    offset = (today.weekday() - THURSDAY) % 7
    last_thursday = today - timedelta(days=offset)
    curr_thursday = last_thursday + timedelta(days=7)
    return [datetime.datetime.strftime(last_thursday, "%Y-%m-%d %H:%M"),
            datetime.datetime.strftime(curr_thursday, "%Y-%m-%d %H:%M")]


class Product:

    def __init__(self, name, cpe):
        self.name = name
        self.cpe = cpe

    def get_cves(self) -> list:
        dates = get_thursdays()
        results = nvdlib.searchCVE(keyword='cpe:2.3:a:microsoft:office:2019:*:*:*:*:*:*:*', modStartDate=dates[0],
                                   modEndDate=dates[1])
        return results
