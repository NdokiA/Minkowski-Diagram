import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import streamlit as st
from PIL import Image
from minkowski import minkowskiDiagram
from marker import add_image_marker

fig, ax = plt.subplots(figsize = (8,8))
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_xlabel('Spatial Coordinate')
ax.set_ylabel('Temporal Coordinate')

fig2, ax2 = plt.subplots(figsize = (8,8))
ax2.set_xlim(-5,5)
ax2.set_ylim(-5,5)
ax2.set_xlabel('Spatial Coordinate')
ax2.set_ylabel('Temporal Coordinate')

t = np.linspace(-100,100,201)
t_hyp = np.linspace(-10,10,200)

mD = minkowskiDiagram(ax, t, t_hyp)
mD2 = minkowskiDiagram(ax2, t, t_hyp)

amg1 = Image.open('images/amogus1.webp').resize((300,300))
amg2 = Image.open('images/amogus2.webp').resize((300,300))

main = st.container()
with main:
    st.markdown("<h1 style = 'margin-bottom: 2rem;'>Minkowski Diagram</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        plot_cones = st.checkbox('Plot Cones', value=True)
    with col2:
        plot_hyperbolas = st.checkbox('Plot Hyperbolas', value=True)
    with col3:
        plot_grid = st.checkbox('Plot Grid', value=True)

    if plot_cones:
        mD.plot_cones()
        mD2.plot_cones()

    if plot_hyperbolas:
        mD.plot_hyperbolas()
        mD2.plot_hyperbolas()
    
    if plot_grid:
        mD.grid()
        mD2.grid()
        
    t_input, x_input = st.columns(2)
    with t_input:
        t_val = st.number_input('Temporal Coordinate', value=0.0)
    with x_input:
        x_val = st.number_input('Spatial Coordinate', value=0.0)
    
    if abs(t_val) > 10:
        st.error("Temporal Coordinate must be between -5 and 5")
    if abs(x_val) > 10:
        st.error("Spatial Coordinate must be between -5 and 5")

    beta = st.slider('Beta', min_value = 0.0, max_value = 0.99, value = 0.0, step = 0.01)
    
    pol1, pol2 = st.tabs(["Event in Moving Frame", "Event in Fixed Frame"])
    with pol1:
        
        
        mD.plot_transformed_grid(beta)
        point = np.array([[x_val], [t_val]])
        point_transformed = mD.coordinate_transform(point, beta)
        
        ax.scatter(x_val, t_val, color = 'blue', marker = 'o', s = 100, label = 'Event')
        add_image_marker(amg1, (x_val, t_val), ax, zoom = 0.1)
        
        ax.scatter(point_transformed[0], point_transformed[1], color = 'red', marker = 'o', s = 100, label = 'Transformed Event')
        add_image_marker(amg2, (point_transformed[0], point_transformed[1]), ax, zoom = 0.1)
        
        origin = np.array([[0],[0]])
        ax.scatter(origin[0], origin[1], marker = 'o', color = 'black',s = 100)
        ax.text(0, 0, 'Origin', fontsize = 12, ha = 'right', va = 'top')

        ax.legend()
        st.pyplot(fig, use_container_width=True)

        st.write(f"Moving Reference Frame: ({point[0][0]:.2f}, {point[1][0]:.2f})")
        st.write(f"Fixed Reference Frame: ({point_transformed[1][0]:.2f}, {point_transformed[0][0]:.2f})")

    with pol2:
        
        mD2.plot_transformed_grid(beta, inverse = False)
        point = np.array([[x_val], [t_val]])
        point_transformed = mD2.coordinate_transform(point, beta, inverse=False)
        
        ax2.scatter(x_val, t_val, color = 'blue', marker = 'o', s = 100, label = 'Event')
        add_image_marker(amg1, (x_val, t_val), ax2, zoom = 0.1)
        
        ax2.scatter(point_transformed[0], point_transformed[1], color = 'red', marker = 'o', s = 100, label = 'Transformed Event')
        add_image_marker(amg2, (point_transformed[0], point_transformed[1]), ax2, zoom = 0.1)
        
        origin = np.array([[0],[0]])
        ax2.scatter(origin[0], origin[1], marker = 'o', color = 'black',s = 100)
        ax2.text(0, 0, 'Origin', fontsize = 12, ha = 'right', va = 'top')

        ax2.legend()
        st.pyplot(fig2, use_container_width=True)

        st.write(f"Fixed Reference Frame: ({point[0][0]:.2f}, {point[1][0]:.2f})")
        st.write(f"Moving Reference Frame: ({point_transformed[1][0]:.2f}, {point_transformed[0][0]:.2f})")

