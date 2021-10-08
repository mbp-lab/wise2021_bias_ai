import numpy as np

# Function to generate a Mesh Grid where feature 1 is x and feature 2 is y
def make_mesh(x, y, padding=.1, h=.005):
    x_min, x_max = x.min()-padding, x.max()+padding
    y_min, y_max = y.min()-padding, y.max()+padding

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy