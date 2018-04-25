import os, json

def _readDataJSON():
    p = os.path.abspath(os.path.join(os.path.dirname(__file__), './data.json'))
    s = ''
    with open(p) as f:
        s += f.read()
    return json.loads(s)

def _checkData(data):
    for year in data:
        for monthDay in data[year]:
            holidayName, weekday = data[year][monthDay]
            if holidayName is False:
                if weekday not in [6, 7]: # Saturday & Sunday
                    raise RuntimeError('Error#1 config in %s: %s' % (year, monthDay))
            elif weekday not in [1, 2, 3, 4, 5]: # Monday ~ Friday
                raise RuntimeError('Error#2 config in %s: %s' % (year, monthDay))


_data = _readDataJSON()
_checkData(_data)

def isHoliday(date):
    year = str(date.year)
    monthDay = date.strftime('%m%d')
    if year not in _data:
        raise RuntimeError('Sorry, can not decide day in year=%s' % year)

    holidayName, _ = _data[year].get(monthDay, [None, None])
    if holidayName is None:
        weekday = date.isoweekday()
        return weekday == 6 or weekday == 7 # Saturday & Sunday are holidays by default
    return holidayName is not False
