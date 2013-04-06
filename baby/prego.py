from datetime import *
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

    def getCountdown(self):
        return "Name : ", self.name,  ", Salary: ", self.salary