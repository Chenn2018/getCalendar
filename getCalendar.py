#coding=utf8
#!/usr/bin/env python
# author: Chenn
# datetime: 2016-05-26

import time
import datetime
import sys

class CalendarObj():
    def __init__(self, year):
        self.year = year
        self.days = []

    def run(self):
        firstDay = datetime.datetime.strptime(self.year + "-01-01", '%Y-%m-%d') # 获取一年中第一天
        lastday = datetime.datetime.strptime(self.year + "-12-31", '%Y-%m-%d') # 获取一年中最后一天
        countday = (lastday - firstDay).days + 1

        for i in range(countday):
            day = firstDay + datetime.timedelta(i)
            self.days.append(time.strftime("%Y-%m-%d", day.timetuple()))

# 查询指定年份的所有日期，格式如：2000-01-01。若没有指定年份，默认为当前年份
if __name__ == "__main__":
    print "START"

    year = time.strftime("%Y", time.localtime())
    if len(sys.argv) == 2:
        year = sys.argv[1]
    elif len(sys.argv) > 2:
        print "参数错误，正确的运行格式为：python getCalendar [year]"
        sys.exit()
    print "查询的年份为: ", year

    calendarObj = CalendarObj(year)
    calendarObj.run()

    print calendarObj.days

    print "END"
