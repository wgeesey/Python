import plotly.express as px
from pathlib import Path  # To save the plot to a specific location.

from die import Die

# Path for saving.
save_path = Path("C:/Users/willi/Desktop/die_visual.png")

# Create a die. Can make any number of die, just need to make some slight changes.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []  # Used to store how many times each value is rolled
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)  # Generate the possible results (2 through 12)
# Loop through the results list, counting the existence of each value (2 through 12)
# then append it to the frequencies list.
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of 1000 rolls of Two D6 (6-sided) die."
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title=dict(text=title, x=0.5, xanchor="center"), xaxis_dtick=1)
fig.show()  # Renders as an HTML file.
# fig.write_html(save_path)

# Can be deleted, since making a histogram; I left it just to verify the histogram
# numbers match up.
print(frequencies)
