seconds = int(input("Enter the number of seconds (from 0 to 8640000): "))

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUER = 60 * 60
SECONDS_IN_DAY = 24 * 60 * 60

days, remainder = divmod(seconds, SECONDS_IN_DAY)
hours, remainder = divmod(remainder, SECONDS_IN_HOUER)
minutes, remainder = divmod(remainder, SECONDS_IN_MINUTE)

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

if days == 1:
    day_word = "day"
elif 2 <= days <= 4:
    day_words = "days"
else:
    day_word = "days"

print(f"{days}, {day_word}, {hours_str}:{minutes_str}:{seconds_str}")