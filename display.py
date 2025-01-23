import numpy as np
import matplotlib.pyplot as plt 
import streamlit as st
from minkowski import minkowskiDiagram

fig, ax = plt.subplots(figsize = (10,10))
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_xlabel('Spatial Coordinate')
ax.set_ylabel('Temporal Coordinate')

t = np.linspace(-100,100,201)
t_hyp = np.linspace(-10,10,200)

mD = minkowskiDiagram(ax, t, t_hyp)

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

    if plot_hyperbolas:
        mD.plot_hyperbolas()
    
    if plot_grid:
        mD.grid()


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
    
    mD.plot_transformed_grid(beta)
    point = np.array([[x_val], [t_val]])
    point_transformed = mD.coordinate_transform(point, beta)
    
    ax.scatter(x_val, t_val, color = 'blue', marker = 'o', s = 100, label = 'Event')

    ax.scatter(point_transformed[0], point_transformed[1], color = 'red', marker = 'o', s = 100, label = 'Transformed Event')

    origin = np.array([[0],[0]])
    ax.scatter(origin[0], origin[1], marker = 'o', color = 'black',s = 100)
    ax.text(0, 0, 'Origin', fontsize = 12, ha = 'right', va = 'top')

    ax.legend()
    st.pyplot(fig, use_container_width=True)

    st.write(f"Original Coordinates: ({point[0][0]:.2f}, {point[1][0]:.2f})")
    st.write(f"Transformed Coordinates: ({point_transformed[1][0]:.2f}, {point_transformed[0][0]:.2f})")


