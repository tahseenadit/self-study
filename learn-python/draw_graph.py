import matplotlib.pyplot as plt
import numpy as np

# Create some example data

"""
The np.linspace(-5, 5, 10) command in Python, using NumPy, generates an array of 10 equally spaced values between -5 and 5 (inclusive). 
Here's what the array looks like:

import numpy as np

values = np.linspace(-5, 5, 10)
print(values)

Output:

[-5.         -3.88888889 -2.77777778 -1.66666667 -0.55555556  0.55555556  1.66666667  2.77777778  3.88888889  5.        ]

In this example, the linspace function creates an array of 10 values, starting from -5 and ending at 5, such that the spacing 
between consecutive values is the same. These values are evenly distributed within the specified range.
"""

x_values = np.linspace(-5, 5, 10)
y_values = x_values**2  # Replace this with your actual function

# Plot the graph
plt.plot(x_values, y_values, label='Graph of y = x^2')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of y = x^2')

# Add gridlines
plt.grid(True)

# Add legend
plt.legend()

# Display the graph
plt.show()