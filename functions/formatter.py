async def format_date(date: str) -> str:
    month = date.split("-")[1]

    if month == "01":
        return f"{date.split('-')[2]} января"
    elif month == "02":
        return f"{date.split('-')[2]} февраля"
    elif month == "03":
        return f"{date.split('-')[2]} марта"
    elif month == "04":
        return f"{date.split('-')[2]} апреля"
    elif month == "05":
        return f"{date.split('-')[2]} мая"
    elif month == "06":
        return f"{date.split('-')[2]} июня"
    elif month == "07":
        return f"{date.split('-')[2]} июля"
    elif month == "08":
        return f"{date.split('-')[2]} августа"
    elif month == "09":
        return f"{date.split('-')[2]} сентября"
    elif month == "10":
        return f"{date.split('-')[2]} октября"
    elif month == "11":
        return f"{date.split('-')[2]} ноября"
    elif month == "12":
        return f"{date.split('-')[2]} декабря"
