# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:56:27 2020

@author: James
"""
import detectface as df

face, eye = df.get_coordinate_pair()
angle_horizontal, angle_vertical = df.calculate_angles(eye, face)
print(angle_horizontal, angle_vertical)
