import datetime

now = datetime.datetime.now()


# 1. strftime() examples:
print("strftime() formats: START ===========================")
print(f"ISO 8601: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Month/Day/Year: {now.strftime('%m/%d/%Y %I:%M %p')}")
print(f"Day, Month Day, Year: {now.strftime('%A, %B %d, %Y')}")
print(f"24-hour clock: {now.strftime('%H:%M')}")
print(f"12-hour clock: {now.strftime('%I:%M %p')}")
print(f"Day of year: {now.strftime('%j')}")
print(f"Day of week (0-6): {now.strftime('%w')}")
print(f"Abbreviated month name: {now.strftime('%b')}")
print(f"Full month name: {now.strftime('%B')}")
print(f"Day of month: {now.strftime('%d')}")
print(f"Hour (24-hour): {now.strftime('%H')}")
print(f"Hour (12-hour): {now.strftime('%I')}")
print(f"Minute: {now.strftime('%M')}")
print(f"Second: {now.strftime('%S')}")
print(f"Microsecond: {now.strftime('%f')}")
print(f"AM/PM: {now.strftime('%p')}")
print(f"Weekday (abbreviated): {now.strftime('%a')}") #Mon, Tue, Wed...
print(f"Year (4 digits): {now.strftime('%Y')}")
print(f"Year (2 digits): {now.strftime('%y')}")
print(f"Timezone name: {now.strftime('%Z')}") # Empty string if no timezone
print(f"Timezone offset: {now.strftime('%z')}") # +HHMM or -HHMM


# 2. f-string examples:
print("\nf-string formats:")
print(f"ISO 8601 in f-string: {now:%Y-%m-%d %H:%M:%S}")
print(f"Custom format in f-string: {now:%B %d, %Y %I:%M %p}")


# 3. isoformat() example:
print("\nisoformat():")
print(f"ISO 8601: {now.isoformat()}")

# Example with microseconds truncated
print(f"ISO 8601 (no microseconds): {now.isoformat(timespec='seconds')}")

# 4. Combining formats:
print("\nCombining formats:")
formatted_date = now.strftime("%B %d, %Y")
formatted_time = now.strftime("%I:%M %p")
print(f"Today is {formatted_date}, and the current time is {formatted_time}.")


# Example with a specific datetime (for consistent output):
specific_datetime = datetime.datetime(2024, 10, 28, 10, 30, 0) # year, month, day, hour, minute, second
print("\nSpecific datetime examples:")
print(f"ISO 8601: {specific_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Month/Day/Year: {specific_datetime.strftime('%m/%d/%Y %I:%M %p')}")
print(f"Day, Month Day, Year: {specific_datetime.strftime('%A, %B %d, %Y')}")