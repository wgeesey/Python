import plotly.express as px

from die import Die

# Create a die.
die = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []  # Used to store how many times each value is rolled
possible_results = range(1, die.num_sides+1)  # Generate the possible results (1 through 6)
# Loop through the results list, counting the existence of each value (1 through 6)
# then append it to the frequencies list.
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of 1000 rolls of a D6 (6-sided) die."
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(title=dict(text=title, x=0.5, xanchor="center"))
fig.show()  # Renders as an HTML file.

# Can be deleted, since making a histogram; I left it just to verify the histogram
# numbers match up.
print(frequencies)