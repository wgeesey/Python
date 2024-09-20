import matplotlib.pyplot as plt
from pathlib import Path  # To save the plot to a specific location.

# Path for saving the plot
save_path = Path("C:/Users/willi/Desktop/scatter_plot.png")


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
# s = size of dots, color can be color=(R, G, B)
# ax.scatter(x_values, y_values, color='red', s=10)
# Colormap example --- the _r means reversed (dark to light/low to high).
# c = values associated with the colormap.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues_r, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])  # min-x, max-x, min-y, max-y

# Optional for plain notation for tick marks.
#  ax.ticklabel_format(style='plain')
plt.show()

# To autosave the graph instead of show it. scatter_plot.png to use the file's directory.
# plt.savefig(save_path, bbox_inches='tight')