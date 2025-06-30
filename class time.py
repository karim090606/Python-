class Time:
    """Represents the time of day using seconds since midnight."""

    def __init__(self, hour=0, minute=0, second=0):
        self.seconds_since_midnight = hour * 3600 + minute * 60 + second

    def __str__(self):
        total_seconds = self.seconds_since_midnight
        minutes, second = divmod(total_seconds, 60)
        hour, minute = divmod(minutes, 60)
        return f"{hour:02}:{minute:02}:{second:02}"

    def time_to_int(self):
        return self.seconds_since_midnight

    def is_after(self, other):
        return self.seconds_since_midnight > other.seconds_since_midnight

    def add_time(self, other):
        total_seconds = self.seconds_since_midnight + other.seconds_since_midnight
        return int_to_time(total_seconds)

    def increment(self, seconds):
        return int_to_time(self.seconds_since_midnight + seconds)

    def is_valid(self):
        return self.seconds_since_midnight >= 0

def int_to_time(seconds):
    return Time(0, 0, seconds)

def print_time(time):
    print(str(time))

def main():
    start = Time(9, 45, 0)
    print("Start time:")
    print_time(start)

    duration = Time(1, 35, 0)
    print("Duration:")
    print_time(duration)

    done = start.add_time(duration)
    print("End time:")
    print_time(done)

    print("Is done after start?", done.is_after(start))

    print("Incremented by 1337 seconds:")
    incr = start.increment(1337)
    print_time(incr)

    print("Is incremented time valid?", incr.is_valid())


if __name__ == "__main__":
    main()
