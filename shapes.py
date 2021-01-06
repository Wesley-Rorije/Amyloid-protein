#!/usr/bin/env python3

"""
Template for the final movie design
"""

__author__ = 'J.A. Busker W.a. Rorije'


from vapory import *


CAMERA = LIGHT = JULIA = first_sec = None

def static_objects():
    """ Create static objects that won't move during the animation"""
    global CAMERA, LIGHT, INTER
    CAMERA = Camera('location', [0, 0, -31], 'look_at', [0, 0, 0])
    
    LIGHT = [LightSource([0, 0, -10], 1)]
    
    #Create the box
    b1 = Box([-20, 20, -1], [20, -3, 6], Pigment('color', [0.8, 0.8, 0]))
    b2 = Box([-20, -20, -1], [20, 10, 6], Pigment('color', [0.4, 1, 0.4]))
    
    #Create the cylinders
    cyl1 = Cylinder([0, -20, 0], [0, -9, 0], 4, Pigment('color', [0.4, 1, 0.4]))
    cyl2 = Cylinder([0, 20, 0], [0, 3, 0], 4, Pigment('color', [0.8, 0.8, 0]))
    
    #Create the ovus
    ovus1 = Ovus(0.85, 0.85, Pigment('color', [0.4, 1, 0.4]), 'rotate', [0, 0, 90], 'scale', 4.0, 'translate', [1.5, -8, -0.5])
    ovus2 = Ovus(0.85, 0.85, Pigment('color', [0.8, 0.8, 0]), 'rotate', [0, 0, 90], 'scale', 4.0, 'translate', [1.5, 2, -0.5])
    
    #Get the intersection of the cylinders/ovus and the box
    INTER = [Intersection(cyl1, b2), Intersection(cyl2, b1), Intersection(ovus1, b2)]
    
    return CAMERA, LIGHT, INTER, Intersection(ovus2, b1)
    
    
