from datetime import datetime, timedelta
import time
class Prego:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getWeeks(self):
        prego_micro = int((time.mktime(self.start.timetuple()) + self.start.microsecond/1000000.0)*1000)
        now_micro = int((time.mktime(self.end.timetuple()) + self.end.microsecond/1000000.0)*1000)
        microseconds = (now_micro - prego_micro)
        week = 1000 * 60 * 60 * 24 * 7
        return microseconds / week

    def getMonths(self):
        #add 1 day to end date to solve different last days of month:
        s1, e1 = self.start, self.end + timedelta(days = 1)
        #convert to 360 days:
        s360 = (s1.year * 12 + s1.month) * 30 + s1.day
        e360 = (e1.year * 12 + e1.month) * 30 + e1.day
        #count days between two 360 dates and return tuple (month/days)
        return divmod(e360 - s360, 30)


    def getCountdown(self):
        return "Name : ", self.name,  ", Salary: ", self.salary