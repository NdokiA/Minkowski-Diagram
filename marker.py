import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def add_image_marker(image, xy, ax, zoom=1):
    img = OffsetImage(image, zoom=zoom)
    ab = AnnotationBbox(img, xy, frameon=False)
    ax.add_artist(ab)