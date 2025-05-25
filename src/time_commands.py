import datetime
import pytz

async def city_time():
    tz_vladivostok = pytz.timezone('Asia/Vladivostok')
    tz_tbilisi = pytz.timezone('Asia/Tbilisi')
    tz_prague = pytz.timezone('Europe/Prague')

    utc_now = datetime.datetime.now(pytz.utc)

    time_format = "%H:%M %p"
    
    vladivostok_time = utc_now.astimezone(tz_vladivostok).strftime(time_format)
    tbilisi_time = utc_now.astimezone(tz_tbilisi).strftime(time_format)
    prague_time = utc_now.astimezone(tz_prague).strftime(time_format)

    response_message = (
        f"**Vladivostok:** {vladivostok_time}\n"
        f"**Tbilisi:** {tbilisi_time}\n"
        f"**Prague:** {prague_time}"
    )

    return response_message