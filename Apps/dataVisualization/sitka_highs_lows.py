from pathlib import Path
import csv
from datetime import datetime


import matplotlib.pyplot as plt


path = Path('weather_data/sitka_weather_2021_simple.csv')
# Read data and get a list of all lines in the file.
lines = path.read_text(encoding='utf-8').splitlines()

# Reader object to parse each line.
reader = csv.reader(lines)
# next(), when given read object returns the next line in the file, starting from the beginning.
# The header row will be assigned here, and printed out, so we see the header information.
header_row = next(reader)

# Prints the index and text of each header row item.
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, high, and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    temperature_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {temperature_date}")
    else:
        dates.append(temperature_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

# Format the plot.
ax.set_title('Daily High and Low Temperatures, 2021', fontsize=24)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

