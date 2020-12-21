import datetime


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.current_time = datetime.datetime(
            1, 1, 1, hour=hours, minute=minutes, second=seconds
        )

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.current_time = datetime.datetime(
            1, 1, 1, hour=hours, minute=minutes, second=seconds
        )

    def get_time(self):
        return f"{self.current_time.time()}"

    def next_second(self):
        self.current_time += datetime.timedelta(seconds=1)
        return self.get_time()


times = Time(23, 59, 59)
print(times.get_time())
print(times.next_second())
print(times.get_time())
