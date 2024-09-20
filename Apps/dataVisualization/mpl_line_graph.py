import matplotlib.pyplot as plt

# Since plot() sets starting data point to x = 0, give it the input values.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Generate one or more plots in same figure.
# fig = represents entire figure; the collection of plots that are generated.
# ax = single plot in the figure.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# Tries to plot the data given in a meaningful way.
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Opens Matplotlib's viewer.
plt.show()