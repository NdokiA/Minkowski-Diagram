# Minkowski Diagram

This project visualizes the Minkowski Diagram for Lorentz transformations using Python and Matplotlib. The Minkowski Diagram is a graphical representation of the Lorentz transformations in special relativity, which describe how the coordinates of an event change under a change of inertial reference frames.

More feature will be added as necessary on this project. 

This project was highly inspired by [Lorentz Transform Visualized](https://mathcube.online/blog/lorentz-transform-visualized/).

## Features

- Plotting light cones
- Plotting hyperbolas
- Plotting a grid
- Interactive coordinate transformation
- Adding image markers to the plot
- Streamlit-based web interface

## Lorentz Transformation

Inverse Lorentz transformation equations on this program defined by

\[ ct = \gamma (ct' + \beta x) \]
\[ x = \gamma (x' + \beta ct) \]

where:
- \( \gamma = \frac{1}{\sqrt{1 - \beta^2}} \)
- \( \beta \) is the velocity as a fraction of the speed of light
- \( ct \) and \( x \) are the temporal and spatial coordinates according to fixed reference frame
- \( ct' \) and \( x' \) are the temporal and spatial coordinates according to moving reference frame

## Usage

### Running the Script

To run the script and visualize the Minkowski Diagram, use the following command:

```sh
streamlit run display.py
```

Or you may access below website [Streamlit] (https://minkowsidiagram.streamlit.app/).

### Interacting with the Diagram

- Use the checkboxes to toggle the plotting of light cones, hyperbolas, and the grid.
- Input the temporal and spatial coordinates to see their transformation.
- Adjust the `beta` slider to change the velocity and see the effect on the coordinates.

## Requirements

The required Python packages are listed in the `requirements.txt` file. Install them using:

```sh
pip install -r requirements.txt
```
## Files

- `display.py`: Main script for visualizing the Minkowski Diagram using Streamlit.
- `minkowski.py`: Contains the `minkowskiDiagram` class for plotting the diagram.
- `marker.py`: Utility functions for adding image markers to the plot.
- `test.py`: Test script for plotting the Minkowski Diagram using Matplotlib.
- `images/`: Directory containing image files used as markers.
