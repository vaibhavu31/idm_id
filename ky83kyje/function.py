import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
 
def imshow(X, resize=None):
    img = Image.fromarray(X)
    if resize:
        
        img = img.resize(resize)
    
    return img.show()