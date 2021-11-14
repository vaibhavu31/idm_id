import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt
 
def imshow(X, resize=None):
    img = Image.fromarray(X)
    if resize:
        
        img = img.resize(resize)
    
    return plt.imshow(img)