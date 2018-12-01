import re,datetime
class Fun():
    def __init__(self):
        pass
    def getActItem(self,parameters):
        time = parameters.get('time')
        place = parameters.get('place')
        date = parameters.get('date')
        act = parameters.get('act')
        time_re = re.search('([0-9]{1,2})[^\d]*([0-9]{1,2})',time)
        hour = int(time_re.group(1))
        min = int(time_re.group(2))
        date_re = re.search('([0-9]{4})-([0-9]{2})-([0-9]{2})',date)
        year = int(date_re.group(1))
        month = int(date_re.group(2))
        day = int(date_re.group(3))
        unix_time = datetime.datetime(year,month,day,hour,min).timestamp()
        date = str(year)+"年"+str(month)+"月"+str(day)+"日"
        time = str(hour)+":"+str(min)
        return act,date,time,place,unix_time
    def getLine(self,org_req):
        room_type = org_req.get('payload').get('data').get('source').get('type')
        if room_type == "group":
            id = org_req.get('payload').get('data').get('source').get('groupId')
        if room_type == "user":
            id = org_req.get('payload').get('data').get('source').get('userId')
        return id
