class MyDate:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if value not in range(1, 32):
            raise ValueError("The day must be 1..31")
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if value not in range(1, 13):
            raise ValueError("The month must be 1..12")
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def add_day(self):
        self.__day += 1
        if self.__day > 31:
            self.__month += 1
            self.__day = 1
        if self.__month > 12:
            self.__year += 1
            self.__month = 1
            self.__day = 1

    def compare_dates(self, my_circle):
        return self.day == my_circle.day and self.month == my_circle.month and self.year == my_circle.year

    def __str__(self):
        return "Число: {} \t Месяц: {} \t Год: {}".format(self.__day, self.__month, self.__year)
