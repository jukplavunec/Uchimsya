SECONDS_IN_DAY = 24 * 60 * 60
SECONDS_IN_HOUR = 60 * 60
SECONDS_IN_MINUTE = 60


def print_timestamp(remaining_seconds):
    time_days = remaining_seconds // SECONDS_IN_DAY
    remaining_seconds = remaining_seconds - time_days * SECONDS_IN_DAY

    time_hours = remaining_seconds // SECONDS_IN_HOUR
    remaining_seconds = remaining_seconds - time_hours * SECONDS_IN_HOUR

    time_minutes = remaining_seconds // SECONDS_IN_MINUTE
    time_seconds = remaining_seconds - time_minutes * SECONDS_IN_MINUTE

    print(f'{time_days}:{time_hours}:{time_minutes}:{time_seconds}')


user_seconds = int(input('Input number of seconds: '))

print_timestamp(user_seconds)